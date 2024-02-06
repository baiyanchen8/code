import matplotlib.pyplot as plt
import cv2
import numpy as np 
names = []
value =[]
im_his = np .zeros (256,dtype= int )
image = cv2.imread('picture/Lena.png')
image =cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
height , width = image.shape
for i in range (height):
    for j in range(width):
        im_his[image[i][j]]+=1

for i in range (len(im_his)):
    names.append(i)
plt.figure(figsize=(6, 6))
plt.bar(names, im_his)
plt.show()