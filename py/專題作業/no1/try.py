Lena= "123456"
x=len(Lena)-5
# ss=bin(Lena)
ss=Lena
tt=ss[:len(ss)-1-x]
t= ss[len(ss)-x:]
ss=tt+'x'+t
print(ss)