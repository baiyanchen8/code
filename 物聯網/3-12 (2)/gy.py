def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                if result[i][j] == 0:
                    result[i][j] = (A[i][k] * B[k][j]) % modnum
                else:
                    result[i][j] = (result[i][j]^(A[i][k] * B[k][j])) % modnum
                # print(f"Partial result at ({i},{j}): {result}")
    return result

def gy_muti(A,B):
    A2=bin(A)[2:].zfill(8)
    B2=bin(B)[2:].zfill(8)
    asd=[0]*16
    for i in range(8):
        for j in range(8):
            a2=int(A2[i])
            b2=int(B2[j])
            ab=a2*b2
            asd[i+j]=asd[i+j]^ab
    asd.reverse()
    dd=""
    for i in asd:
        dd=dd+str(i)
    
    return dd

print(gy_muti(0x02,0x6b))
matrix = [
    [0x7C, 0x6B, 0x01, 0xD7],
    [0xF2, 0x30, 0xFE, 0x63],
    [0x2B, 0x76, 0x7B, 0xC5],
    [0xAB, 0x77, 0x6F, 0x67],
]

normalmatrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

modnum = int(0b100011011)

print(matrix_multiplication(normalmatrix, matrix))
