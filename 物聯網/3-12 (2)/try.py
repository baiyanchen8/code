import math
def me1thod(va):
    if va <= 1 :
        return "EXCEPTION\n"
    k=0        
    for i in range(2,math.floor(math.sqrt(va)+1)):
        k+=1
        if va % i ==0 and i!=va:
            return "COMPOSITE\n"
    return f"PRIME {k}\n"


# 讀取 input.txt 檔案
with open('input.txt', 'r') as file:
    # 將每行讀取並轉換為整數，存入列表
    numbers = [int(line.strip()) for line in file]

asd=[me1thod(i) for i in numbers]
with open('output.txt', 'w') as file:
    # 將每行讀取並轉換為整數，存入列表
    for i in asd:
        file.write(i)
