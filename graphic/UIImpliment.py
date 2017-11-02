# -*- coding = utf-8 -*-

'''
实现UI界面的逻辑信号连接等
ui文件“graphicUI.py

'''
from PyQt5.QtWidgets import QTabBar

from graphicUI_withtab import *
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui
from actionImpliment import *
from PyQt5.Qt import QImage, QPixmap, QSize
# opencv 临时添加
from opencvImpliment import IopenCV
from cv2 import *
import opencvLibrary as ol


class uiWindows(Ui_MainWindow, QFileDialog):
	_signal = QtCore.pyqtSignal(str)
	def __init__(self, Window):
		super(Ui_MainWindow, self).__init__()
		Ui_MainWindow.setupUi(self,Window)
		#self.actionOpen.triggered.connect(self.sendName)
		self.buttonBind()
		#self._signal.connect(self.test)
		self.cvImgList = []
		self.tabImages = {}

	def buttonBind(self):
		'''按键和函数绑定'''
		# File
		self.actionNew.triggered.connect(self.addNew)
		#self.actionOpen.triggered.connect(menuAction.openFile)
		self.actionOpen.triggered.connect(self.openfile)
		self.actionSave.triggered.connect(menuAction.saveFile)
		self.actionSave_as.triggered.connect(menuAction.saveAsFile)
		self.actionClose.triggered.connect(menuAction.closeFile)
		self.actionRecent.triggered.connect(menuAction.recentFiles)

		# Show

		#Tran
		self.actionToGray.triggered.connect(self.toGray)

		# sharpen
		self.actionSharpen.triggered.connect(self.sharpen)

		#edge
		self.actionRoberts.triggered.connect(self.roberts)

		# 临时放的一个关闭标签的按钮
		self.menuCloseTab.triggered.connect(self.closeTab)


	def openfile(self):
		# getOpenFileName的filter 文件类型使用空格隔开,条目使用双分号隔开
		fileFilter = 'Image File(*.jpg *.bmp *.png);;All Files(*)'
		fileName, fileType = QFileDialog.getOpenFileName(self, 'Open file', './', fileFilter)
		if fileName:
			cvImg = ol.readImg(fileName)
			self.showCVimgInNewTab(cvImg)
			# self.showImgInNewTab(self.cvImg2Qimg(cvImg),fileName.split('/')[-1])

	def getImgFromTab(self):
		# tabID = self.tabWidget.currentIndex()
		# tabName = self.tabWidget.currentWidget().objectName()
		return self.tabImages[self.tabWidget.currentWidget().objectName()]



	def addNew(self):
		print(self.tabWidget.currentWidget().objectName())

	def showImg(self,Qimage, label='left'):
		'''
		显示图片
		:param label:显示的label o 原始图片，a 转换后的图片
		:return:None
		'''
		if label == 'left':
			'''
			# 添加的一下语句是尝试对图片适应label。
			#tempWidth tempHeight 自适应的宽和高
			Himg = Qimage.height()
			Wimg = Qimage.width()
			Hlb = self.image1.height()
			Wlb = self.image1.width()
			tempWidth = Qimage.height()/self.image1.height()*self.image1.width()
			tempHeight = Qimage.width()/self.image1.width()*self.image1.height()
			if tempHeight > self.image1.height():
				Qimage.scaledToHeight(self.image1.height())
				Qimage.scaledToWidth(tempWidth/100)
			elif tempWidth > self.image1.width():
				Qimage.scaledToHeight(tempHeight/100)
				Qimage.scaledToWidth(self.image1.width())
			else:
				print("not Match")
			Himg2 = Qimage.height()
			Wimg2 = Qimage.width()
			# 自适应 end '''
			# 叹了一句，还有这种操作，上面的都是废话了。
			self.image1.setPixmap(QPixmap.fromImage(Qimage).scaled(self.image1.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation))
			# self.image1.resize(QSize(Qimage.width(),Qimage.height()))
		elif label == 'right':
			self.image2.setPixmap(QPixmap.fromImage(Qimage).scaled(self.image2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
		elif label == 'new':
			self.addTab(Qimage,'hahahah')

	def showImgInNewTab(self,Qimage, tabName=''):
		self.addTab(Qimage, tabName)

	def showCVobjInNewTab(self, IcvObject, tabName=''):
		self.cvImgList.append(IcvObject)
		self.addTab(IcvObject.cvImg2Qimg(IcvObject.getImgData()),tabName)

	def showCVimgInNewTab(self,cvImg,tabName=""):
		if tabName == "":
			tabName = 'New' + str(self.tabWidget.count() + 1)
		self.addTab(self.cvImg2Qimg(cvImg), tabName)
		self.tabImages[self.tabWidget.currentWidget().objectName()] = cvImg

	def addTab(self,Qimage, tabName = ''):
		tabCount = self.tabWidget.count()
		tabNew = QtWidgets.QWidget()
		tabNew.setEnabled(True)
		tabNew.setAcceptDrops(True)
		tabNew_name = "tab"+str(tabCount+1)
		tabNew.setObjectName(tabNew_name)
		labelNew = QtWidgets.QLabel(tabNew)
		labelNew.setGeometry(QtCore.QRect(0, 0, 1001, 571))
		labelNew.setText("")
		labelNew.setAlignment(QtCore.Qt.AlignCenter)
		labelNew.setObjectName("label"+str(tabCount+1))
		if not tabName == '':
			tabNew_name = tabName
		self.tabWidget.addTab(tabNew, tabNew_name)
		labelNew.setPixmap(
			QPixmap.fromImage(Qimage).scaled(labelNew.size(),
			                                 Qt.KeepAspectRatio,
			                                 Qt.SmoothTransformation))
		self.tabWidget.setCurrentWidget(tabNew)

	def closeTab(self):
		name = self.tabWidget.objectName()
		print(self.tabWidget.objectName())
		#tabID = self.tabWidget.currentIndex()
		#self.tabWidget.removeTab(tabID)

	def getCurrentTabID(self):
		return self.tabWidget.currentIndex()

	def toGray(self):
		gray = ol.colorToGray(self.getImgFromTab())
		self.showCVimgInNewTab(gray,"")


	def cvImg2Qimg(self,cvImg):
		#height, width, colorDepth = cvImg.shape

		# 真彩色
		if len(cvImg.shape) == 3:
			height, width, colorDepth = cvImg.shape
			byteValue = colorDepth * width
			cvtColor(cvImg, COLOR_BGR2RGB,cvImg)
			return QImage(cvImg, width, height, byteValue, QImage.Format_RGB888)
		# 灰度图
		elif len(cvImg.shape) == 2:
			height, width = cvImg.shape
			byteValue = width
			#gray = cvtColor(cvImg, COLOR_BGR2GRAY)  #进来已经是灰度图了，不需要再转一次
			return QImage(cvImg,width,height,byteValue,QImage.Format_Indexed8)

	def sharpen(self):
		sharpenImg = ol.sharpen(self.getImgFromTab())
		self.showCVimgInNewTab(sharpenImg,'')

	def edgeDect(self):
		self.showCVimgInNewTab(ol.edgeDetect(self.getImgFromTab()))

	def roberts(self):
		self.showCVimgInNewTab(ol.edgeRoberts(self.getImgFromTab()))
