import math
def D2B(p,w):
    arr = []
    for i in range(w):
        k= p%2
        p=math.floor(p/2)
        arr.append(k)
    arr.reverse()
    return arr
print(D2B(73,8))
