import  cv2
import random
import numpy as np
image = cv2.imread('picture\Lena.png')
# 圖型轉字符
height, width, _ = image.shape
resized_image = cv2.resize(image, (82,82))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
height, width, _ = resized_image.shape

a0= ['Q','w','7','.']
a1=['@','O','v',':']
a=[63,127,191,256]
f=open('matlab6/img1.txt',"w")

mat= np.zeros((height,width),dtype= int)


# 加密內容
for x in range (height):
    for y in range(width):
        mat[x][y]= random.randint(0,1)


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
        else:
            f.write(a1[k]+' ')
    f.write('\n')
f.close()


# 偽裝圖解密
f2=open('matlab6/img1.txt',"r")
mat2= np.zeros((height,width),dtype= int)
j=0
k=0
for line in f2.readlines():
    arr=[i for i in line.split(' ')]
    for j in range(82):
        if a0.count(arr[j])>0:
            mat2[k][j]=0
        else:
            mat2[k][j]=1
    k+=1    
f2.close()
# 對比
for x in range (height):
    for y in range(width):
        if mat[x][y]!=mat2[x][y]:
            print('error') 