def flod(arr):
    x=[]
    for i in range(int(len(arr)/2)):
        x.append(arr[i] ^ arr[i+int(len(arr)/2)]) 
    return x
arr = [ 0,0,1,0,0,1,1,1,1,1]
print(arr)
print(flod(arr=arr))