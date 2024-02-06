import cv2
import numpy as np 
import matplotlib.pyplot as plt
image = cv2.imread('picture/Lena.png')

image =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

height,width=image.shape
new_im =np.zeros((height,width),dtype= int)
new_im2 = np.zeros((height,width),dtype= int)
def Max(i,j):
    if i>j:
        return i
    else :
        return j
def Min(i,j):
    if i>j:
        return j
    else :
        return i

for i in range (height):
    for j in range(width):
        if i==0 or j ==0:
            new_im[i][j]=image[i][j]
        else :
            left = image[i][j-1]
            up = image[i-1][j]
            left_up=image[i-1][j-1]
            if left_up >= Max(up,left):
                new_im[i][j] = Min(up,left)
            elif left_up <= Min(up,left):
                new_im[i][j] = Max(up,left)
            else: 
                new_im[i][j]=int(left)+int(up)-int(left_up)
            new_im[i][j]=image[i][j]-new_im[i][j]
            new_im2[i][j] = image[i][j] - round((int(left_up)+int(left)+int(up))/3)
            
            
for i in range (height):
    for j in range(width):
        predict=0
        if i==0 or j ==0:
            predict=0
        else :
            left = image[i][j-1]
            up = image[i-1][j]
            left_up=image[i-1][j-1]
            if left_up >= Max(up,left):
                predict = Min(up,left)
            elif left_up <= Min(up,left):
                predict = Max(up,left)
            else: 
                predict=int(left)+int(up)-int(left_up)
        if predict+new_im[i][j]!= image[i][j]:
            exit('error')

name1 =[] 
name2 =[]
names=[]
min1 =0 
max1 =0 
min2 =0 
max2 =0 
for i in range (1,height):
    for j  in range (1,width):
        pixel =int(new_im[i][j])
        name1.append(pixel)
        if max1 < pixel:
            max1 = pixel
        if min1 > pixel:
            min1 = pixel

for i in range (1,height):
    for j  in range (1,width):
        pixel =int(new_im2[i][j])
        name2.append(pixel)
        if max2 < pixel:
            max2 = pixel
        if min2 > pixel:
            min2 = pixel

if min1 < min2 :
    min = min1
else :
    min=min2
if max1 >max2 :
    max = max1
else :
    max=max2
value1=[]  
value2=[] 
for i in range(min,max+1):
    names.append(i)
    value1.append(name1.count(i))
    value2.append(name2.count(i))
x = np.linspace(min, max,209)
plt.figure(figsize=(6, 6))
plt.plot(x,value1,c='red')
plt.plot(x,value2)
plt.show()