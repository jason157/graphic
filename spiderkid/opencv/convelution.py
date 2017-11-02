# -*- coding = uft-8

import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np

#img = plt.imread("../face2.jpg")                        #在这里读取图片
img = cv2.imread("../lena.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("image",img)
cv2.imshow("gray", gray)

sharpKernel = np.array([
	[ -1, -1, -1],                        #这个是设置的滤波，也就是卷积核
	[ -1,  8, -1],
	[ -1, -1, -1]
])
sharpKernelL = np.array([
	[ -1, -1, -1, -1, -1],                        #这个是设置的滤波，也就是卷积核
	[ -1,  2,  2,  2, -1],
	[ -1,  2,  2,  2, -1],
	[ -1,  2,  2,  2, -1],
	[ -1, -1, -1, -1, -1]
])

edgeKernelX = np.array([
	[ 1, 2, 1],
	[ 0, 0, 0],
	[-1,-2,-1]
])
edgeKernelY = np.array([
	[1, 0,-1],
	[2, 0,-2],
	[1, 0,-1]
])
shadeKernel = np.array([
	[1, 1, 1, 0, 0],
	[1, 1, 1, 0, 0],
	[1, 1, 1, -1, -1],
	[0, 0, -1, -1 ,-1],
	[0, 0, -1, -1, -1]
])
c_s = cv2.flip(shadeKernel,-1)


res_sharp = cv2.filter2D(img,-2,sharpKernel)                      #使用opencv的卷积函数
res_sharpL = cv2.filter2D(gray,-2,sharpKernelL)

res_gray = cv2.filter2D(gray,-1,sharpKernel)

res_edge_x = cv2.filter2D(gray, -1, edgeKernelX)
res_edge_y = cv2.filter2D(gray, -1, edgeKernelY)

res_shade = cv2.filter2D(gray, -1, shadeKernel)
res_c_s = cv2.filter2D(gray, -1, c_s)
print(c_s)
canny = cv2.Canny(img,200,240)

# cv2.imshow("res_sharp",res_sharp)
# cv2.imshow("res_sharpL",res_sharpL)
#cv2.imshow("res_gray",res_gray)
#cv2.imshow("res_edge_x",res_edge_x)
#cv2.imshow("res_edge_y",res_edge_y)
cv2.imshow("res_shade",res_shade)
cv2.imshow("res_c_s",res_c_s)

# x_y = cv2.add(res_edge_x,res_edge_y)
# cv2.imshow("x+y",x_y)
# cv2.imshow("canny",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()