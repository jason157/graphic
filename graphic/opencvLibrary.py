from cv2 import *
import numpy as np
import os

def readImg(filePath):
	if not os.path.exists(filePath):
		return None
	return imread(filePath)


def colorToGray(cvImg):
	if len(cvImg.shape) is not 3:
		return 0
	return cvtColor(cvImg,COLOR_BGR2GRAY)

def sharpen(cvImg):
	laplacianKernel = np.array([
		[0, -1, 0],
		[-1, 5, -1],
		[0, -1, 0]])
	return filter2D(cvImg,-1,laplacianKernel)

def edgeDetect(cvImg):
	return Canny(cvImg,200,256)

def edgeRoberts(cvImg):
	pass


def deal(cvImg):
	pass