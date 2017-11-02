# -*- coding = utf-8 -*-
'''opencv的实现部分

'''

from cv2 import *
import os

from PyQt5.QtGui import QImage


class IopenCV:
	def __init__(self,filePath=None,cvimg=None):
		self._imgData = None
		if cvimg is not None:
			self._imgData = cvimg

		if filePath is not None:
			self.__loadImgToData(filePath)

		#self._mQImage = None

		#self.__cvImag2Qimage(self._imgData)

	def __loadImgToData(self,filePath):
		if not os.path.exists(filePath):
			return False
		try:
			self._imgData = imread(filePath)
		except Exception as e:
			return False
		else:
			if not self._imgData is None:
				return True
		return False

	def getImgData(self):
		return self._imgData

	def __cvImag2Qimage(self,cvImg):
		'''
		图像从cv mat 转换为 QImage
		:param cvImg:
		:return: QImage
		'''
		height, width, byteValue = cvImg.shape
		# byValue? 啥啥东西，上面的byValue = 3 3个字节的东西，24位真彩图片
		#这里一乘，就是一列的宽度？
		byteValue = byteValue * width
		#颜色转换，从BGR->RGB
		cvtColor(cvImg, COLOR_BGR2RGB, cvImg)
		# 从cv图像转换到Qt图像
		return  QImage(cvImg, width, height, byteValue, QImage.Format_RGB888)

	@staticmethod
	def cvImg2Qimg(cvImg):
		height, width, colorDepth = cvImg.shape

		# 真彩色
		if colorDepth == 3:
			byteValue = colorDepth * width
			cvtColor(cvImg, COLOR_BGR2RGB,cvImg)
			return QImage(cvImg, width, height, byteValue, QImage.Format_RGB888)
		elif colorDepth is None:
			byteValue = width
			gray = cvtColor(cvImg, COLOR_BGR2GRAY)
			return QImage(gray,width,height,byteValue,QImage.Format_Indexed8)



	def cvImg2Qimg(self,cvimg):
		return self.__cvImag2Qimage(cvimg)

	def getQimge(self):
		return self.__cvImag2Qimage(self._imgData)

	def __qImg2cvImg(self, Qimage):
		'''
		Qimage 转 cvImag ## 思考：是否有数据丢失？
		:param Qimage:
		:return:
		'''
		pass

	def toGray(self):
		# 转灰度图
		cvtColor(self._imgData,COLOR_BGR2GRAY,self._imgData )





