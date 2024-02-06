import numpy as np
import random 
arr=[i for i in range(1,101)]
random.shuffle(arr)

for i in range(len(arr)-1,0,-1):
    for j in range(i,-1,-1):
        if arr[j]>arr[i]:
            tmp =arr[j]
            arr[j]=arr[i]
            arr[i]=tmp
        
print(arr)