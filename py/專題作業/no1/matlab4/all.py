# 1
import math
def D2B(p,w=0):
    arr = []
    for i in range(8):
        k= p%2
        p=math.floor(p/2)
        arr.append(k)
    arr.reverse()
    for i in range(w):
        arr.pop()
    return arr
print(D2B(25,0))
print(D2B(25,1))
def D2B2(p):
    arr = []
    while(p>0):
        k= p%2
        p=math.floor(p/2)
        arr.append(k)
    arr.reverse()
    return arr

# 2
def B2D(bits):
    sum=0
    for i in range(len(bits)):
        sum+= bits[len(bits)-1-i]*(2**i)
    return sum
print (B2D(D2B(25,1)))
# print(B2D([1,1,0,0]))

# 3
def LsBset(p,massage):
    arr=[]
    for i  in bin(p)[2:]:
        arr.append(int(i))
    for i in range(len(massage)):
        arr[len(arr)-i-1]=massage[len(massage)-i-1]
    ans=B2D(arr)
    return ans
# print(LsBset(155,[1,0,1]))


# 4
def LsBget(p,w):
    arr=[]
    for i  in bin(p)[2:]:
        arr.append(int(i))
    ans=arr[len(arr)-w:]
    return ans
print(LsBget(157,3))