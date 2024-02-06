def B2D(bits):
    sum=0
    for i in range(len(bits)):
        sum+= bits[len(bits)-1-i]*(2**i)
    return sum
print (B2D([1,0,0,0,0,0]))
        