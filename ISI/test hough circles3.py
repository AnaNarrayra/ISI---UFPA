# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:39:16 2017

@author: Ana
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('14-8_cam_2_image_3.tif',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
output = cimg.copy()

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1.5, 1700)


circles = np.uint16(np.around(circles))
for (x, y, r) in circles[0,:]:
    # draw the outer circle
    cv2.circle(output,(x, y), int(1.82*r),(0,255,0),3)
    # draw the center of the circle
    cv2.circle(output,(x,y),2,(0,0,255),4)
plt.imshow(output)
plt.show()

crop_img = output[1027:1127, 44:278]

plt.imshow(crop_img)
#plt.imshow(np.hstack([output, crop_img]))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
#12-37_cam_1_image_1
#14-8_cam_2_image_3
#'detected circles',