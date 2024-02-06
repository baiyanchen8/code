import math
import numpy as np 
import random

M = 10000
N = 100
max_X=10000
min_X =0
max_Y=10000
min_Y=0
point  = np.zeros((M,2), dtype = float)
gravitycenter= np.zeros((N,2), dtype = float)
matrix = np.zeros((M,N), dtype = float)

for i in range(M):
    point[i][0] = random.randint(min_X,max_X)
    point[i][1] = random.randint(min_Y,max_Y)

def countdist():
    for i in range (N):
        for j in range (M):
            deltax=point[j][0]-gravitycenter[i][0]
            deltay=point[j][1]-gravitycenter[i][1]
            matrix[j][i]=(deltax**2+deltay**2)**0.5
            
def Gravitycenter():
    newgravitycenter= np.zeros((N,2), dtype = float)
    numofarr=np.zeros(N, dtype = int)
    whereis=np.zeros(M, dtype = int)
    for  i in range (M):
        mini=0
        # pick 離i最近的重心
        for j in range (N):
            if matrix[i][j]<matrix[i][mini]:
                mini=j
        newgravitycenter[mini][0]+=point[i][0]
        newgravitycenter[mini][1]+=point[i][1]
        numofarr[mini]+=1
        whereis[i]=mini

    for j in range (N):
        if numofarr[j]!=0:
            newgravitycenter[j][0]/=numofarr[j]
            newgravitycenter[j][1]/=numofarr[j]
    different=0
    for j in range (N):
        if  gravitycenter[j][0]!=newgravitycenter[j][0] or gravitycenter[j][1]!=newgravitycenter[j][1]:
            different+=1
    if different >0:
        print('=================================')
        print(whereis)
        print(newgravitycenter)
        print(gravitycenter)
        for j in range (N):
            gravitycenter[j][0]=newgravitycenter[j][0] 
            gravitycenter[j][1]=newgravitycenter[j][1]
        countdist()
        Gravitycenter()
    else:
        print('=================================')
        print(whereis)
        print(newgravitycenter)
        print('-----------------------------')
        print(gravitycenter)

# first run 
for i in range(N):
    x = random.randint(0,M-1)
    gravitycenter[i][0]=float(point[x][0])
    gravitycenter[i][1]=float(point[x][1])
countdist()
Gravitycenter()