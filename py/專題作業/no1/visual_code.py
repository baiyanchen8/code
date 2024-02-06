import cv2
import numpy as np
import random


# orgin image 
origin_img = cv2.imread('picture/ghost.png')
origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
origin_img=cv2.resize(origin_img,(256,256))
print ( origin_img.shape)
xxx=256
yyy= 256
# 建立全黑的新圖片 269*474
shape =(xxx*2, yyy*2, 3)# y, x, RGB
new_A = np.zeros(shape, np.uint8)
x,y= origin_img.shape
for i in range (xxx):
    for j in range (yyy):
        list1 = [0,1,2,3]
        random.shuffle(list1)
        if list1[0]==0 or list1 [1] ==0 :
            new_A[i*2,j*2]=255
        else :
            new_A[i*2,j*2]=3
        
        if list1[0]==1 or list1 [1] ==1 :
            new_A[i*2+1,j*2]=255
        else :
            new_A[i*2+1,j*2]=3
        
        if list1[0]==2 or list1 [1] ==2 :
            new_A[i*2,j*2+1]=255
        else :
            new_A[i*2,j*2+1]=3
            
        if list1[0]==3 or list1 [1] ==3 :
            new_A[i*2+1,j*2+1]=255
        else :
            new_A[i*2+1,j*2+1]=3
cv2.imshow('Image', new_A)
cv2.waitKey(0)
cv2.destroyAllWindows()

shape =(xxx*2, yyy*2, 3)# y, x, RGB
new_B = np.zeros(shape, np.uint8)
for i in range (xxx):
    for j in range (yyy):
        if (origin_img[i,j]> 128):
            new_B [i*2,j*2]=new_A[i*2,j*2]
            new_B [i*2,j*2+1]=new_A[i*2,j*2+1]
            new_B [i*2+1,j*2]=new_A[i*2+1,j*2]
            new_B [i*2+1,j*2+1]=new_A[i*2+1,j*2+1]
        else :
            
            if new_A[i*2,j*2][1]==3:
                new_B [i*2,j*2]=255
            else:
                new_B [i*2,j*2]=3
                
            if new_A[i*2,j*2+1][0]==3:
                new_B [i*2,j*2+1]=255
            else:
                new_B [i*2,j*2+1][0]=3
                
            if new_A[i*2+1,j*2][0]==3:
                new_B [i*2+1,j*2]=255
            else:
                new_B [i*2+1,j*2]=3
                
            if new_A[i*2+1,j*2+1][0]==3:
                new_B [i*2+1,j*2+1]=255
            else:
                new_B [i*2+1,j*2+1]=3

cv2.imshow('Image', new_B)
cv2.waitKey(0)
cv2.destroyAllWindows()

shape =(xxx*2, yyy*2, 3)# y, x, RGB
new_C = np.zeros(shape, np.uint8)
for i in range (xxx*2):
    for j in range (yyy*2):
        if new_A[i,j][0] ==3 or new_B[i,j][0] ==3 :
            new_C[i,j] =0
        else :
            new_C[i,j]=255
        # print(new_C[i,j])
cv2.imshow('Image', new_C)
cv2.waitKey(0)
cv2.destroyAllWindows()