# -*- coding = utf-8 -*-

import cv2
import numpy as np



def draw_circle(event, x, y, flags, count):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		# color(B, G, R)
		circle_color = (0, 0, 255)
		cv2.circle(img, (x, y),100,circle_color, 1)
		print(globals())
	elif event == cv2.EVENT_RBUTTONDBLCLK:
		if count == 0:
			point1 = (x, y)
			count = 1
			print("r 1:",count)
		else:
			line_color = (255, 0, 0)
			cv2.line(img, point1, (x, y), line_color,1)
			count = 0
			print("r 2:",count)
	elif event == cv2.EVENT_RBUTTONDOWN:
		line_color = (255, 0, 0)
		cv2.line(img, (x,y), (x+2, y+2), line_color, 2)


count = 0
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle,count)

while True:
	cv2.imshow("image",img)
	if cv2.waitKey(20)&0xFF == 27:
		break
cv2.destroyAllWindows()