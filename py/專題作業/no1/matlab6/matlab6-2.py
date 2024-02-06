import  cv2
import random
import numpy as np
image = cv2.imread('picture\Lena.png')
# 圖型轉字符
height, width, _ = image.shape
resized_image = cv2.resize(image, (82,82))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
height, width, _ = resized_image.shape

a0=['Q','W','7','.']
a1=['@','V','I','o']
a2=['E','Z','1','c']
a3=['0','X','T','r']
a=[63,127,191,256]
f=open('matlab6/img2.txt',"w")

mat= np.zeros((height,width),dtype= int)


# 加密內容
for x in range (height):
    for y in range(width):
        mat[x][y]= random.randint(0,3)
# 偽裝圖生成
for x in range (height):
    arr=[]
    for y in range(width):
        k=0
        pixel=gray_image[x,y]
        while pixel>a[k]:
            k+=1
        if mat[x][y]==0:
            f.write(a0[k]+' ')
        elif mat[x][y]==1:
            f.write(a1[k]+' ')
        elif mat[x][y]==2:
            f.write(a2[k]+' ')
        elif mat[x][y]==3:
            f.write(a3[k]+' ')
    f.write('\n')
f.close()


# 偽裝圖解密
f2=open('matlab6/img2.txt',"r")
mat2= np.zeros((height,width),dtype= int)
j=0
k=0
for line in f2.readlines():
    arr=[i for i in line.split(' ')]
    for j in range(82):
        if a0.count(arr[j])!=0:
            mat2[k][j]=0
        elif a1.count(arr[j])!=0:
            mat2[k][j]=1
        elif a2.count(arr[j])!=0:
            mat2[k][j]=2
        elif a3.count(arr[j])!=0:
            mat2[k][j]=3
    k+=1    
f2.close()



# 對比
for x in range (height):
    for y in range(width):
        if mat[x][y]==mat2[x][y]:
            print('0')
        else:
            print('1',mat[x][y],mat2[x][y])