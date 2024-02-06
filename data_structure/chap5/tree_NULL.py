'''
用於證明 
分支度為 k 
共有 n 個node 的tree 共有 n(k-1)+1 個空連接
'''
import random
class simulator:
    def __init__(self,n,k):
        self.n=n-1
        self.k=k
        self.all=0

    def simulation (self):
        numofkid=0
        for _ in range(self.k):
            h=random.randint(0,1)
            if h==1 and self.n>0:
                numofkid+=1
                self.n-=1
        self.all+=(self.k-numofkid)
        print(self.all)
        for _ in range(numofkid):
            self.simulation()

    def verify(self):
        if self.all==(self.k-1)*self.n+1:
            return True
        else:
            return False
n,k=3,2
test=simulator(n,k)
test.simulation()
print(test.all)
print(test.verify(),((k-1)*n)+1)