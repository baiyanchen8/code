import cv2
import numpy as np
import math
image = cv2.imread('picture\Lena.png')

height, width,_= image.shape()
image = cv2.resize(image, (round(width), round(height)))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width= image.shape()




# 切割大小
block = 128
sHeight =math.ceil(height/block)
sWidth =math.ceil(width/block)
def en(Ii):
    sum=0
    num=0
    for y in range(len(Ii)):
        for x in range(len(Ii[0])):
            sum+=Ii[y][x]
            num+=1
    if num!=0:
        aver=sum/(num)
    upsum=0
    upnum=0
    downsum=0
    downnum=0
    for y in range(len(Ii)):
        for x in range(len(Ii[0])):
            if Ii[y][x] >= aver:
                upsum+=Ii[y][x]
                upnum+=1
                Ii[y][x]=1
            else :
                downsum+=Ii[y][x]
                downnum+=1
                Ii[y][x]=0
    if upnum!=0:
        upaver=upsum/upnum
    if downnum!=0:
        downaver=downsum/downnum
    else :
        downaver =upaver
    return Ii,upaver,downaver

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
            if y+block > height:
                ymax = height
            else :
                ymax = y+block
                
            if x+block >= width:
                xmax = width
            else :
                xmax = x +block
            Ii=mat01[y:ymax,x:xmax]
            Bi,ai,bi=en(Ii)
            for y1 in range(y,ymax):
                for x1 in range(x,xmax):
                    mat01[y1][x1]=Bi[y1-y][x1-x]
            yy=math.floor(y/block)
            xx=math.floor(x/block)
            upAvermat[yy,xx]=ai
            downAvermat[yy,xx]=bi
    return mat01,upAvermat,downAvermat

def de (Bi,ai,bi):
    for y in range(len(Bi)):
        for x in range(len(Bi[0])):
            if Bi[y][x]==0:
                Bi[y][x]=bi
            else:
                Bi[y][x]=ai
    return Bi
    
def AMBTCde(mat01,upAvermat,downAvermat):  
    new_image = np.zeros(image.shape, np.uint8) 
    for y in range(0,height,block):
        for x in range(0,width,block):
            if y+block > height:
                ymax = height
            else :
                ymax = y+block
                
            if x+block >= width:
                xmax = width
            else :
                xmax = x +block
            yy=math.floor(y/block)
            xx=math.floor(x/block)
            Bi=mat01[y:ymax,x:xmax]
            Ci=de(Bi,upAvermat[yy][xx],downAvermat[yy][xx])
            for y1 in range(y,ymax):
                for x1 in range(x,xmax):
                    new_image[y1][x1]=Ci[y1-y][x1-x]
    return new_image

Bi,ai,bi=AMBTCen(image=image)
new_image=AMBTCde(Bi,ai,bi) 

cv2.imshow('Image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
