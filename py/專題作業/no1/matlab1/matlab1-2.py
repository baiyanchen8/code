mat =[
    [20,31,25,40],
    [34,51,39,42],
    [37,55,53,60]
]
s=[1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0]
k=-0
for i in range(3):
    for j in range (4):
        # 字串處理
        ss=bin(mat[i][j])
        tt=ss[:len(ss)-2]
        ss=tt+str(s[k])
        ss=ss+str(s[k+1])
        mat[i][j]=int(ss[2:],2)
        k+=2
print(mat)