import cv2 
import numpy as np 
import random
import math 
# 基礎參數設定
B =64
Cb ={2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:4,13:5,14:4,15:4,16:6,
     64:14}
refer_table=np.zeros((256,256), dtype = int)
image = cv2.imread('picture/Tiffany.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_2 = cv2.imread('picture/Tiffany.png')
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
height,width = image.shape
insert_table=np.zeros((height,width), dtype = int)
for r in range(256): #y
    for c  in range (256): #x 
        refer_table[r][c]=(Cb[B]*r +c)%B

sum=0 # sum of pixel
for r in range(height): #y
    for c  in range (0,width,2): #x 
        sum+=2
        new = random.randint(0,B-1)
        p1=image[r][c]
        p2=image[r][c+1]
        edge =0
        if abs(refer_table[p1][p2]-new) <= abs(B+new-refer_table[p1][p2]):
            edge =abs(refer_table[p1][p2] - new)
        else: 
            edge = abs(B+new-refer_table[p1][p2])
        if edge > abs(B-new+refer_table[p1][p2]):
            edge =abs(B-new+refer_table[p1][p2])
        dist = edge 
        if p1 - edge >0:
            rmin =p1-edge 
        else :
            rmin = 0
        if p1 + edge<256:
            rmax = p1 + edge
        else :
            rmax=255
        if p2 - edge >0:
            cmin =p2-edge 
        else :
            cmin = 0
        if p2 + edge<256:
            cmax = p2 + edge
        else :
            cmax=255
        ansr=0
        ansc=0
        for r1 in range(rmin,rmax+1):
            for c1 in range (cmin,cmax+1):
                if refer_table[r1][c1]==new and (((r1-p1)**2+(c1-p2)**2)**0.5)  <=dist: 
                    dist = ((r1-p1)**2+(c1-p2)**2)**0.5
                    ansr=r1
                    ansc=c1
        image[r][c]=ansr
        image[r][c+1]=ansc

MSE=0.0
for i in range(height):
    for j in range(width):
        MSE+=(image[i][j] -image_2[i][j])*(image[i][j] -image_2[i][j])/sum

k=255**2
k/=MSE
PSNR = math.log10(k)
PSNR*=10
print(PSNR)