# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphic.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
'''

'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 511, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(510, 0, 511, 501))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")
        self.menuTran = QtWidgets.QMenu(self.menubar)
        self.menuTran.setObjectName("menuTran")
        self.menuEnhance = QtWidgets.QMenu(self.menubar)
        self.menuEnhance.setObjectName("menuEnhance")
        self.menuEdgeDetection = QtWidgets.QMenu(self.menubar)
        self.menuEdgeDetection.setObjectName("menuEdgeDetection")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setCheckable(False)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionScan = QtWidgets.QAction(MainWindow)
        self.actionScan.setObjectName("actionScan")
        self.actionSlide = QtWidgets.QAction(MainWindow)
        self.actionSlide.setObjectName("actionSlide")
        self.actionXmirror = QtWidgets.QAction(MainWindow)
        self.actionXmirror.setObjectName("actionXmirror")
        self.actionYmirror = QtWidgets.QAction(MainWindow)
        self.actionYmirror.setObjectName("actionYmirror")
        self.actionFadeIN = QtWidgets.QAction(MainWindow)
        self.actionFadeIN.setObjectName("actionFadeIN")
        self.actionClock90 = QtWidgets.QAction(MainWindow)
        self.actionClock90.setObjectName("actionClock90")
        self.actionAntiClock90 = QtWidgets.QAction(MainWindow)
        self.actionAntiClock90.setObjectName("actionAntiClock90")
        self.actionClock180 = QtWidgets.QAction(MainWindow)
        self.actionClock180.setObjectName("actionClock180")
        self.actionToGray = QtWidgets.QAction(MainWindow)
        self.actionToGray.setObjectName("actionToGray")
        self.action256to8bits = QtWidgets.QAction(MainWindow)
        self.action256to8bits.setObjectName("action256to8bits")
        self.actionToBin = QtWidgets.QAction(MainWindow)
        self.actionToBin.setObjectName("actionToBin")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUage = QtWidgets.QAction(MainWindow)
        self.actionUage.setObjectName("actionUage")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionContour = QtWidgets.QAction(MainWindow)
        self.actionContour.setObjectName("actionContour")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionRecent)
        self.menuShow.addAction(self.actionScan)
        self.menuShow.addAction(self.actionSlide)
        self.menuShow.addAction(self.actionXmirror)
        self.menuShow.addAction(self.actionYmirror)
        self.menuShow.addAction(self.actionFadeIN)
        self.menuShow.addAction(self.actionClock90)
        self.menuShow.addAction(self.actionAntiClock90)
        self.menuShow.addAction(self.actionClock180)
        self.menuTran.addAction(self.actionToGray)
        self.menuTran.addAction(self.action256to8bits)
        self.menuTran.addAction(self.actionToBin)
        self.menuEnhance.addAction(self.actionSharpen)
        self.menuEdgeDetection.addAction(self.actionRoberts)
        self.menuEdgeDetection.addAction(self.actionContour)
        self.menuHelp.addAction(self.actionUage)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuTran.menuAction())
        self.menubar.addAction(self.menuEnhance.menuAction())
        self.menubar.addAction(self.menuEdgeDetection.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.setStatusBar("Ready")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.menuTran.setTitle(_translate("MainWindow", "Trans"))
        self.menuEnhance.setTitle(_translate("MainWindow", "Enhance"))
        self.menuEdgeDetection.setTitle(_translate("MainWindow", "EdgeDetection"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionRecent.setText(_translate("MainWindow", "recent"))
        self.actionScan.setText(_translate("MainWindow", "Scan"))
        self.actionSlide.setText(_translate("MainWindow", "Slide"))
        self.actionXmirror.setText(_translate("MainWindow", "Xmirror"))
        self.actionYmirror.setText(_translate("MainWindow", "Ymirror"))
        self.actionFadeIN.setText(_translate("MainWindow", "FadeIn"))
        self.actionClock90.setText(_translate("MainWindow", "Clock90"))
        self.actionAntiClock90.setText(_translate("MainWindow", "AntiClock90"))
        self.actionClock180.setText(_translate("MainWindow", "Clock180"))
        self.actionToGray.setText(_translate("MainWindow", "toGray"))
        self.action256to8bits.setText(_translate("MainWindow", "256to8bits"))
        self.actionToBin.setText(_translate("MainWindow", "toBin"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUage.setText(_translate("MainWindow", "Uage"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionContour.setText(_translate("MainWindow", "Contour"))

    def setStatusBar(self,string):
        self.statusbar.showMessage(string)

