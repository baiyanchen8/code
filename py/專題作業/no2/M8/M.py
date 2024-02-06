import cv2
import numpy as np 
import random
image = cv2.imread('picture/Lena.png')

image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

height,width=image.shape
new_im =np.zeros((height,width),dtype= np.uint8)
S=[]
def block(B):
    global S
    p =[[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],(1,1)]
    e = np.zeros((3,3),dtype=int)
    for i in range(9):
        e[p[i][0],p[i][1]]=B[p[i][0]][p[i][1]]-B[1][1]
    for i in range(8):
        if e[p[i][0],p[i][1]]==0:
            S.append(random.randint(0,1))
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]+S[len(S)-1]
        elif e[p[i][0],p[i][1]]==-1:
            S.append(random.randint(0,1))
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]-S[len(S)-1]
        elif e[p[i][0],p[i][1]]>0:
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]+1
        elif e[p[i][0],p[i][1]]<-1:
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]-1
    return e

for i in range(0,height,3):
    for j in range(0,width,3):
        b=  np.zeros((3,3),dtype=int)
        imax =i+3
        jmax = j+3
        if imax>=height :
            continue
        if jmax>=width :
            continue
        for i1 in range(i,imax):
            for j1 in range(j,jmax):
                b[i1-i][j1-j]=image[i1][j1]
        e= block(b)
        for i1 in range(i,imax):
            for j1 in range(j,jmax):
                new_im[i1][j1]=b[1][1]+e[i1-i][j1-j]

cv2.imshow('Image', new_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
S2=[]
def decrypt(B):
    global S2
    p =[[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],(1,1)]
    e=  np.zeros((3,3),dtype=int)
    for i in range(9):
        e[p[i][0],p[i][1]]=B[p[i][0]][p[i][1]]-B[1][1]
    for i in range (8):
        if e[p[i][0],p[i][1]]==0 or e[p[i][0],p[i][1]] ==-1:
            S2.append(0)
        elif e[p[i][0],p[i][1]]==1 or e[p[i][0],p[i][1]] ==-2:
            S2.append(1)
        if e[p[i][0],p[i][1]]>0:
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]-1
        elif e[p[i][0],p[i][1]]<-1:
            e[p[i][0],p[i][1]]=e[p[i][0],p[i][1]]+1
        else:
            pass
    return e


for i in range(0,height,3):
    for j in range(0,width,3):
        b=  np.zeros((3,3),dtype=int)
        imax =i+3
        jmax = j+3
        if imax>=height :
            continue
        if jmax>=width :
            continue
        for i1 in range(i,imax):
            for j1 in range(j,jmax):
                b[i1-i][j1-j]=new_im[i1][j1]
        e= decrypt(b)
        for i1 in range(i,imax):
            for j1 in range(j,jmax):
                new_im[i1][j1]=b[1][1]+e[i1-i][j1-j]
        
cv2.imshow('Image', new_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(len(S2)):
    if S2[i]!=S[i]:
        exit('error')