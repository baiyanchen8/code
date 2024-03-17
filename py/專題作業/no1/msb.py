import cv2
import numpy as np
import random
origin_img = cv2.imread('picture/Lena.png')
origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
origin_img=cv2.resize(origin_img,(256,256))
x,y=origin_img.shape
for i in range (x):
    for j in range (y):
        if origin_img[i][j]>128:
            origin_img[i][j]=255
        else:
            origin_img[i][j]=0
cv2.imshow('Image', origin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()