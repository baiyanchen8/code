import cv2 
import hashlib
import math 
image = cv2.imread('picture/Lena.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
origin = cv2.imread('picture/Lena.png')
origin=cv2.cvtColor(origin,cv2.COLOR_BGR2GRAY)
height,width =image.shape
k=3 #嵌入幾位
n=4
def flod(arr):
    x=[]
    for i in range(int(len(arr)/2)):
        x.append(arr[i] ^ arr[i+int(len(arr)/2)]) 
    return x
def hash_arr(arr):
    md5_hash = hashlib.md5( repr(tuple(arr)).encode()).digest()
    binary_hash = ''.join(format(byte, '08b') for byte in md5_hash)
    x=[]
    for i in  binary_hash:
        x.append(int(i))
    return x
def B2D(bits):
    sum=0
    for i in range(len(bits)):
        sum+= bits[len(bits)-1-i]*(2**i)
    return sum
def D2B(msg,k):
    binary = bin(msg)[2:]
    binary=binary.zfill(k)
    x=[]
    for i in binary:
        x.append(int(i))
    return x
def kLsb(msg,k):
    x=D2B(msg,8)
    return x[len(x)-k:]
def kMsb(msg,k):
    x=D2B(msg,8)
    return x[:k]


for i in range (0,height,n):
    for j in range(0,width,n):
        #  i&i+1
        #  j&j+1
        arr=[]
        for x in range(n):
            for y in range(n):
                arr.append(image[i+x][j+y])
        msb=[]
        for x in range(len(arr)):
            msb.append(B2D(kMsb(arr[x],8-k)))
        hashcode=hash_arr(msb)
        
        while len(hashcode)>2*(n**2)*k:
            hashcode= flod(hashcode)
        if len(hashcode)>(n**2)*k:
            hashcode=hashcode[:(n**2)*k]
            
        for x in range(len(arr)):
            msb[x]=D2B(msb[x],8-k)
            for y in range(x*k,(x+1)*(k)):
                msb[x].append(hashcode[y])
            arr[x]=B2D(msb[x])
        sum=0
        for x in range(n):
            for y in range(n):
                image[i+x][j+y]=arr[sum]
                sum+=1
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
sum = height*width
MSE=0.0
for i in range(height):
    for j in range(width):
        MSE+=(int(image[i][j]) -int(origin[i][j]))**2/sum
print(image[6][4])
k=255**2
k/=MSE
PSNR = math.log10(k)
PSNR*=10
print(PSNR)
        
        
