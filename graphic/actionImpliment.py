# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
# openfiledialog.py

from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QTextEdit
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# from UIImpliment import uiWindows


class menuAction(QFileDialog):
	'''实现Gui的菜单响应函数'''
	def __init__(self, parent=None):
		super(menuAction,self).__init__(parent)
		pass

	def openFile(self):
		'''打开文件'''
		file = ''
		try:
			# file = QFileDialog.getOpenFileName(self, caption="open file",directory='/',options=None)
			print(self)
			fileName, filetype = QFileDialog.getOpenFileName(self,
			                                                 "QFileDialog.getOpenFileName()",
			                                                 "hahah",
			                                                 "All Files (*);;Text Files (*.txt)")
		except Exception as e:
			print(e)
		#file, ok = QFileDialog.getOpenFileName(self,caption="tile",directory=".",filter="ImageFiles(*.jpg *.png *.bmp",options=None)
		print("打开文件",file)

	def createNewFile(self):
		pass

	def saveFile(self):
		pass

	def saveAsFile(self):
		pass

	def closeFile(self):
		pass

	def recentFiles(self):
		pass

