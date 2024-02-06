from  method import sudo_random
from  method import mat_to_arr
from  method import arr_to_mat
from  method import PSNR_calculator
import random
import numpy 
import cv2
import math

image = cv2.imread('picture\Lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width= image.shape
mat_sudo =numpy.zeros((256,256),dtype= int)
sudo=sudo_random.sudoku_return()

for i in range(256):
    for j in range(256):
        mat_sudo[i][j]= sudo[i%9][j%9]-1


def ceh(MAT,secret,x,y):
    candidate =[]
    candidatex=[]
    if x <=3:
        for i in range(9):
            candidate.append(MAT[i][y])
            candidatex.append(i)
    elif x<252:
        c= [-4,-3,-2,-1,0,1,2,3,4]
        for i in range(9):
           candidate.append(MAT[x+c[i]][y])
           candidatex.append(x+c[i])
    else :
        for i in range(9):
            candidate.append(MAT[247+i][y]) 
            candidatex.append(247+i)
    ansx=0
    for i in range(9):
        if candidate[i]==secret:
            ansx=candidatex[i]
            return ansx,y
    print("ceh false")
def cev(MAT,secret,x,y):
    candidate =[]
    candidatey=[]
    if y <=3:
        for i in range(9):
            candidate.append(MAT[x][i])
            candidatey.append(i)
    elif y<252:
        c= [-4,-3,-2,-1,0,1,2,3,4]
        for i in range(9):
           candidate.append(MAT[x][y+c[i]]) 
           candidatey.append(y+c[i])
    else :
        for i in range(9):
            candidate.append(MAT[x][247+i]) 
            candidatey.append(247+i)
    ansy=0
    for i in range(9):
        if candidate[i]==secret:
            ansy=candidatey[i]
            return x,ansy
    print("cev false")
    print(candidate)
        
def ceb(MAT,secret,x,y):
    if x <252 and y <255:
        candidate =[]
        candidatx =[]
        candidaty =[]
        ansx=0
        ansy=0
        xb =math.floor((x)/3)*3
        yb =math.floor((y)/3)*3
        for i in range(3):
            for j in range(3):
                candidate.append(MAT[xb+i][yb+j])
                candidatx.append(xb+i)
                candidaty.append(yb+j)
        for i in range(9):
            if candidate[i]==secret:
                ansx=candidatx[i]
                ansy=candidaty[i]
                return ansx,ansy
        print("ceb error")
        print(candidate)
    return None
    
arr = mat_to_arr.mat_to_arr(image)
# print(arr)
secret=[]
for i in range(int(len(arr)/2)):
    secret.append(random.randint(0,8))
for i in range(0,len(arr),2):

        x=arr[i]
        y=arr[i+1]
        if ceb(mat_sudo,secret[int(i/2)],x,y)==None:
            cehx,cehy=ceh(mat_sudo,secret[int(i/2)],x,y)
            cevx,cevy=cev(mat_sudo,secret[int(i/2)],x,y)
            deltah=abs(cehx-x)+abs(cehy-y)
            deltav=abs(cevx-x)+abs(cevy-y)
            if (deltah<=deltav):
                arr[i]=cehx
                arr[i+1]=cehy
            if (deltav<=deltah):
                arr[i]=cevx
                arr[i+1]=cevy
        else:
            cehx,cehy=ceh(mat_sudo,secret[int(i/2)],x,y)
            cevx,cevy=cev(mat_sudo,secret[int(i/2)],x,y)
            cebx,ceby=ceb(mat_sudo,secret[int(i/2)],x,y)
            deltah=abs(cehx-x)+abs(cehy-y)
            deltav=abs(cevx-x)+abs(cevy-y)
            deltab=abs(cebx-x)+abs(ceby-y)
            if (deltah<=deltab and deltah <=deltav):
                arr[i]=cehx
                arr[i+1]=cehy
            if (deltab<=deltah and deltab <=deltav):
                arr[i]=cebx
                arr[i+1]=ceby
            if (deltav<=deltah and deltav <=deltab):
                arr[i]=cevx
                arr[i+1]=cevy
kkk =arr_to_mat.arr_to_mat(arr,height,width)
new_image = numpy.zeros(image.shape, numpy.uint8) 
for i in range(height):
    for j in range (width):
        new_image[i][j]= kkk[i][j]
# cv2.imshow('Image', new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("psnr=",PSNR_calculator.PSNR(image,new_image))