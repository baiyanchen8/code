from  method import *
import random
import numpy as np
import cv2
import math

ts_mark= np.zeros((256,256),dtype= int)
ts_num= np.zeros((256,256),dtype= int)
ts_num[0][0]=0
for i in range (256):
    if i>0:
        if i%2==0:
            ts_num[i][0]=(ts_num[i-1][0]+3)%8
        else :
            ts_num[i][0]=(ts_num[i-1][0]+2)%8
    for j in range (1,256):
        ts_num[i][j]=(ts_num[i][j-1]+1)%8

# how to fix turtle shell mark
# it is a big problem
# 1 is inside 2 is edge of turtle shell, 3 is  edge of matrix 
se = [[7,4],[1,6],[3,0],[5,2]]

for i in range(256):
    for j in range (256):
        for k in range(4):
            if i>=1 and i+2<256 and j >=1 and j <=254:
                if ts_num[i][j]==se[k][1] and ts_num[i+1][j]==se[k][0]  :
                    ts_mark[i-1][j] =2
                    ts_mark[i][j] =1
                    ts_mark[i+1][j] =1
                    ts_mark[i+2][j] =2
                    ts_mark[i][j+1] =2
                    ts_mark[i][j-1] =2
                    ts_mark[i+1][j+1] =2
                    ts_mark[i+1][j-1] =2
                elif ts_num[i-1][j]==se[k][1] and ts_num[i][j]==se[k][0] :
                    pass
            else :
                ts_mark[i][j] = 3

for i in range(255,0,-1):
    for j in range (255,0,-1):
        for k in range(4):
            if i>=1 and i+2<256 and j >=1 and j <=254:
                if ts_num[i][j]==se[k][1] and ts_num[i+1][j]==se[k][0]  :
                    ts_mark[i-1][j] =2
                    ts_mark[i][j] =1
                    ts_mark[i+1][j] =1
                    ts_mark[i+2][j] =2
                    ts_mark[i][j+1] =2
                    ts_mark[i][j-1] =2
                    ts_mark[i+1][j+1] =2
                    ts_mark[i+1][j-1] =2
                elif ts_num[i-1][j]==se[k][1] and ts_num[i][j]==se[k][0] :
                    pass
            else :
                ts_mark[i][j] = 3
                
    # rewrite
def ch1(secret,x,y):
    if ts_mark[x+1][y] ==2 :
            candi =[(x,y),(x+1,y),(x-1,y),(x-2,y),(x,y+1),(x+1,y+1),(x,y-1),(x+1,y-1)]
            for i in range(8):
                zz= candi[i]
                if ts_num[zz[0]][zz[1]]== secret:
                    return zz[0],zz[1]                    
    else :
        candi =[(x,y),(x+1,y),(x+2,y),(x-1,y),(x,y+1),(x+1,y+1),(x,y-1),(x+1,y-1)]
        for i in range(8):
            zz= candi[i]
            if ts_num[zz[0]][zz[1]]== secret:
                return zz[0],zz[1]   


def ch2(secret,x,y):
    pass
def ch3(secret,x,y):
    pass
            
            
image = cv2.imread('picture\Lena.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width= image.shape

im_arr=mat_to_arr.mat_to_arr(image) 
xx=int(len(im_arr)/2)
secret =np.zeros((xx),dtype=int)
for i in range(xx):
    secret[i]=random.randint(0,7)
# for i in range (xx):
#     im_arr[2*i],im_arr[2*i+1]=che(secret[i],im_arr[2*i],im_arr[2*i+1])
kk= arr_to_mat.arr_to_mat(im_arr,height,width)
