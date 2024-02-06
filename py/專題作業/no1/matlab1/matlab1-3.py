import cv2
import numpy as np
Baboon=cv2.imread('picture/Baboon.tif')
Baboon = cv2.cvtColor(Baboon, cv2.COLOR_BGR2GRAY)
Lena=cv2.imread('picture/Lena.png')
Lena = cv2.cvtColor(Lena, cv2.COLOR_BGR2GRAY)
# a
mat_Baboon= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if Baboon[i][j]>=128 :
            mat_Baboon[i][j]= 1
        else :
            mat_Baboon[i][j]= 0
# b
mat_Baboon_show= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if mat_Baboon[i][j]==1 :
            mat_Baboon_show[i][j]= 255 
        else :
            mat_Baboon_show[i][j]= 0
# cv2.imshow('b',mat_Baboon_show)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# c
Stego = np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if mat_Baboon[i][j]==0:
            Stego[i][j]=Lena[i][j]  &~1 
        else :    
            Stego[i][j]=Lena[i][j]  | 1
# cv2.imshow('c',Stego)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# d
mat_Stego= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if Stego[i][j]&1 ==1:
            mat_Stego[i][j] = 1 
        else:
            mat_Stego[i][j]=  0
mat_Stego_show= np.zeros((512,512), np.uint8)
for i in range(512):
    for j in range(512):
        if mat_Stego[i][j]==1:
            mat_Stego_show[i][j]= 255 
        else :
            mat_Stego_show[i][j]= 0
# cv2.imshow('d',mat_Stego_show)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ESS
newLena= np.zeros((512,512), np.uint8)
for x in range(8):
    for i in range(512):
        for j in range (512):
            # 字串處理
            ss=bin(Lena[i][j])[2:]
            ss.zfill(8)
            if len(ss)-x-1>=0:
                tt=ss[:len(ss)-x-1]
            else :
                tt=''
            t=ss[len(ss)-x:]
            xx=tt+str(mat_Stego[i][j])+t
            newLena[i][j]=int(xx,2)
    cv2.imshow('e'+str(x+1),newLena)
    cv2.waitKey(0)
    cv2.destroyAllWindows()