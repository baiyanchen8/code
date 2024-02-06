import numpy as np
import random 
arr=[i for i in range(1,101)]
random.shuffle(arr)
longs = len(arr)
for i in range(longs):
    small =i
    for j in range(i,longs):
        if arr[small]>arr[j]:
            small =j
    arr[i],arr[small]=arr[small],arr[i]
print(arr)