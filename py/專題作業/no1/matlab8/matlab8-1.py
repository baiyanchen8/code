import cv2
import numpy as np
import math
image = cv2.imread('picture\coolpick.jpg')

height, width, _ = image.shape
image = cv2.resize(image, (round(width*0.5), round(height*0.5)))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width= image.shape




# 切割大小
block = 128
sHeight =math.ceil(height/block)
sWidth =math.ceil(width/block)

def AMBTCen(image):
    mat01 = np.zeros((height,width), dtype = int)
    upAvermat =np.zeros((sHeight,sWidth), dtype = int)
    downAvermat =np.zeros((sHeight,sWidth), dtype = int)
    for y in range(0,height):
        for x in range(0,width):
            pixel = image [y,x]
            mat01[y,x]=pixel
    for y in range(0,height,block):
        for x in range(0,width,block):
            sum,num=0,0
            if y+block > height:
                ymax = height
            else :
                ymax = y+block
                
            if x+block >= width:
                xmax = width
            else :
                xmax = x +block
            for y1 in range(y,ymax):
                for x1 in range(x,xmax):
                    sum+=mat01[y1][x1]
                    num+=1
            if num!=0:
                aver=sum/(num)
            upsum=0
            upnum=0
            downsum=0
            downnum=0
            for y1 in range(y,ymax):
                for x1 in range(x,xmax):
                    if mat01[y1][x1] >= aver:
                        upsum+=mat01[y1][x1]
                        upnum+=1
                        mat01[y1][x1]=1
                    else :
                        downsum+=mat01[y1][x1]
                        downnum+=1
                        mat01[y1][x1]=0
            if upnum!=0:
                upaver=upsum/upnum
            if downnum!=0:
                downaver=downsum/downnum
            else :
                downaver =-1
            yy=math.floor(y/block)
            xx=math.floor(x/block)
            upAvermat[yy,xx]=upaver
            downAvermat[yy,xx]=downaver
    return mat01,upAvermat,downAvermat
        
def de(mat01,upAvermat,downAvermat):  
    new_image = np.zeros(image.shape, np.uint8) 
    for y in range (height):
        for x in range (width):
            yy=math.floor(y/block)
            xx=math.floor(x/block)
            if mat01[y][x]==0:
                new_image[y][x]=downAvermat[yy][xx]
            else:
                new_image[y][x]=upAvermat[yy][xx]
    return new_image

Bi,ai,bi=AMBTCen(image=image)
new_image=de(Bi,ai,bi) 

cv2.imshow('Image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
