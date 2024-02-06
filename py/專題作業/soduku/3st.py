from  method import sudo_random
from  method import mat_to_arr
from  method import arr_to_mat
import random
import numpy 
import cv2
import math
from  method import PSNR_calculator
image = cv2.imread('picture\Lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width= image.shape
mat_sudo =numpy.zeros((256,256),dtype= int)
sudo =numpy.zeros((256,256),dtype= int)
sudo=sudo_random.sudoku_return()
# print(sudo)
for i in range(256):
    for j in range(256):
        mat_sudo[i][j]= sudo[i%3][j%3]-1

def ceb(MAT,secret,x,y):
    candidate =[]
    candidatx =[]
    candidaty =[]
    xb =math.floor((x)/9)*9
    yb =math.floor((y)/9)*9
    for i in range(9):

        for j in range(9):
            if xb+i <=255 and yb+j <=255:
                if MAT[xb+i][yb+j]==secret:
                    candidatx.append(xb+i)
                    candidaty.append(yb+j)
                    candidate.append((xb+i-x)**2+(yb+j-y)**2)
    small=0
    for i in range(len(candidate)):
        if(candidate[i]<candidate[small]):
            small=i
    # print(candidatx[small],candidaty[small])
    return candidatx[small],candidaty[small]


arr = mat_to_arr.mat_to_arr(image)
# print(arr)
secret=[]
for i in range(int(len(arr)/2)):
    secret.append(random.randint(0,8))
# capacity didn't control
for i in range(0,len(arr),2):
    arr[i],arr[i+1]=ceb(mat_sudo,secret[int(i/2)],arr[i],arr[i+1])

kkk =arr_to_mat.arr_to_mat(arr,height,width)
new_image = numpy.zeros(image.shape, numpy.uint8) 
for i in range(height):
    for j in range (width):
        new_image[i][j]= kkk[i][j]
cv2.imshow('Image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("psnr=",PSNR_calculator.PSNR(image,new_image))