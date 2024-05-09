def gcd(a,b):
    while (b>0):
        q= int(a/b)
        r= a%b # also equal a-b*q
        a=b
        b=r
    return a

print(gcd(4,2))