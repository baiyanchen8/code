import cv2 as cv
import numpy as np
import random 
import math
import time
image = cv.imread('picture/Tiffany.png')
height,width,_= image.shape

N= 32 # 調色盤顏色數量
M = height*width # pixel 數量
point  = []
point2  = []
gravitycenter=[]
whereis=np.zeros(M, dtype = int)
matrix = np.zeros((M,N), dtype = float)
num1=0
sum=0
for i in range(height):
    for j in range (width):
        pixel = image[i][j]
        point.append(pixel)
        point2.append(pixel)
        sum+=1
# pick initial center

for i in range(N):
    x = random.randint(0,M-1)
    arr=[point[x][0],point[x][1],point[x][2]]
    while gravitycenter.count(arr)>0:
        x = random.randint(0,M-1)
        arr=[point[x][0],point[x][1],point[x][2]]
    gravitycenter.append(arr)

if len(gravitycenter)!= N:
    exit('false')

def countdist():
    global point
    global gravitycenter
    for i in range (N):
        for j in range (M):
            arr=gravitycenter[i]
            a1=point[j]
            deltar=int(a1[0])-int(arr[0])
            deltag=int(a1[1])-int(arr[1])
            deltab=int(a1[2])-int(arr[2])
            matrix[j][i]=(deltar**2+deltag**2+deltab**2)**0.5
countdist()

def Gravitycenter():
    global num1
    global gravitycenter
    global whereis
    newgravitycenter= np.zeros((N,3), dtype = int)
    numofarr=np.zeros(N, dtype = int)
    
    for  i in range (M):
        mini=0
        # pick 離i最近的重心
        for j in range (N):
            if matrix[i][j]<matrix[i][mini]:
                mini=j
        newgravitycenter[mini][0]+=point[i][0]
        newgravitycenter[mini][1]+=point[i][1]
        newgravitycenter[mini][2]+=point[i][2]
        numofarr[mini]+=1
        whereis[i]=mini
    different=0
    for j in range (N):
        
        newgravitycenter[j][0]=round(newgravitycenter[j][0]/numofarr[j])
        newgravitycenter[j][1]=round(newgravitycenter[j][1]/numofarr[j])
        newgravitycenter[j][2]=round(newgravitycenter[j][2]/numofarr[j])
    
        if  newgravitycenter[j][0]!=gravitycenter[j][0] or newgravitycenter[j][1]!=gravitycenter[j][1] or newgravitycenter[j][2]!=gravitycenter[j][2]:
            different+=1
            gravitycenter[j][0]=newgravitycenter[j][0] 
            gravitycenter[j][1]=newgravitycenter[j][1]
            gravitycenter[j][2]=newgravitycenter[j][2]
            
    if different >0:
        # print('=================================')
        print(num1)
        print(whereis)
        # print(newgravitycenter)
        print(gravitycenter)            
        num1+=1
        countdist()
        Gravitycenter()
    else:
        print('=================================')
        print(num1)
        print(whereis)
        # print(newgravitycenter)
        print(gravitycenter)
        print('------------END-----------------')
        
Gravitycenter()