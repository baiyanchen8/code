import cv2
import numpy as np
import random 
im = cv2.imread('picture/Lena.png')
pixel=np.zeros((256),dtype= int )
im =cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
h,w=im.shape
for i in range (h):
    for j in range(w):
        pi = im[i][j]
        pixel[pi]+=1
max = 0
zero=[]
for i in range(256):
    if pixel[i] == 0:
        zero.append(i)
    if pixel[i] > pixel[max]:
        max=i
   
near =0
for i in range(len(zero)):
    if abs(max-zero[i])< abs(max-near):
        near=zero[i]

secret = np .zeros(pixel[max],dtype= int )
for i in range (pixel[max]):
    secret[i] =random.randint(0,1)
if max >= near :
    sum=0
    for i in range (h):
        for j in range(w):
            if im[i][j] > near and im[i][j] < max :
                im[i][j]-=1
            if im[i][j]==max:
                if secret[sum]==1:
                    im[i][j]-=1
                sum+=1
else :
    sum=0
    for i in range (h):
        for j in range(w):
            if im[i][j] < near and im[i][j] > max :
                im[i][j]+=1
            if im[i][j]==max:
                if secret[sum]==1:
                    im[i][j]+=1
                sum+=1

cv2.imshow('Image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
sum=0
for i in range (h):
        for j in range(w):
            
            if im[i][j]==max and secret[sum]==1:
                print('error')
            if im[i][j]==max-1 and secret[sum]==0:
                print('error')
            if im[i][j]==max or  im[i][j]==max-1:
                sum+=1