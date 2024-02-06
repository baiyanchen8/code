import numpy as np
def mat_to_arr(MAT):
    height=len(MAT)
    width =len(MAT[0])
    ans =np.zeros((height*width),dtype=int)
    k=0
    for i in range(height):
        for j in range(width):
            ans[k]=MAT[i][j]
            k=k+1
    return ans
