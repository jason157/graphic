
import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

# img = cv2.imread('face2.jpg')

# print('type:',type(img))
# r, g, b = cv2.split(img)
# img2 = deepcopy(img)

# x往下 y往右
# img[x, y]
# img2[0:50,0:100] = 0
#matplot 使用的是RGB cv2使用的是BGR
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)

# plt.subplot(121),plt.imshow(img),plt.title('origin')
# plt.subplot(122),plt.imshow(img2),plt.title('after')
# plt.show()
# cv2.imshow('name', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pic1 = cv2.imread('pic1.png')
pic2 = cv2.imread('pic2.png')

