import numpy as np
def arr_to_mat(arr,h,w):
    mat= np.zeros((h,w),dtype= int)
    k=0
    for i in range(h):
        for j in range(w):
            mat[i][j]=arr[k]
            k=k+1
    return mat