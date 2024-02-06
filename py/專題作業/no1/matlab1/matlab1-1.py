mat =[
    [20,31,25,40],
    [34,51,39,42],
    [37,55,53,60]
]
s=[1,0,0,1,1,0,0,0,1,1,0,0]
k=-1
for i in range(3):
    for j in range (4):
        k+=1
        if s[k]==1:
            mat[i][j] = mat[i][j] | 1
        else:
            mat[i][j] = mat[i][j] & ~1
print(mat)