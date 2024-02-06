
import keyboard as kb
class kbmanager():
    def __init__(self) :
        self.functions={}
        self.superkey=[]
        
    def __call__(self):
        kb.on_press(self.input_manager)
    def add_new_keyfunc(self,key,func):
        if self.functions.get(key) ==None:
            self.functions[key]=func
    
    def input_manager(self,key):
        for i in range(len(self.superkey)):
            if key.name == self.superkey[i]:
                print(key.name)
                self.functions[self.superkey[i]]()
                return
            
    def delte_keyfunc(self,key):
        if self.functions.get(key,default=None) !=None:
            self.functions.pop(key)

    def keyShow(self):
        print(self.functions)
    
