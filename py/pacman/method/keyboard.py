import keyboard as kb
class kbcontroller():
    def __init__(self) :
        self.key="aaa"
        self.pause=False
        self.tmp_key=""
        self.change_key=False
        self.list=["up","down","left","right","pause","speedup"]
        self.board={
            "up":"up",
            "down":"down",
            "left":"left",
            "right":"right",
            "speedup":"a",
            "pause":"p"
        }
    def pp(self):
        self.key="aaa"
    def change(self,x):
        num=0
        for i in range(6):
            if self.board[self.list[i]] == x.name:
                num+=1
        if num==0 and self.tmp_key!="":
            self.board[self.tmp_key]=x.name
        self.change_key=True
        
    def lka(self,x):
        print(x.name)
        if x.event_type =='up':
            self.key="aaa"
        if self.key==x.name:
            return None
        k_up=kb.KeyboardEvent(name=self.board["up"],scan_code=0,event_type='down')
        k_down=kb.KeyboardEvent(name=self.board["down"],scan_code=0,event_type='down')
        k_left=kb.KeyboardEvent(name=self.board["left"],scan_code=0,event_type='down')
        k_rihgt=kb.KeyboardEvent(name=self.board["right"],scan_code=0,event_type='down')
        k_speedup=kb.KeyboardEvent(name=self.board["speedup"],scan_code=0,event_type='down')
        k_p_down=kb.KeyboardEvent(name=self.board["pause"],scan_code=0,event_type='down')
        if x.name==k_up.name and x.event_type==k_up.event_type and self.pause==False:
            self.key=self.board["up"]
        elif x.name==k_down.name and x.event_type ==k_down.event_type :
            self.key=self.board["down"]
        elif x.name==k_left.name and x.event_type ==k_left.event_type :
            self.key=self.board["left"]
        elif x.name==k_rihgt.name and x.event_type ==k_rihgt.event_type :
            self.key=self.board["right"]
        elif x.name ==k_speedup.name and x.event_type ==k_speedup.event_type :
            self.key=self.board["speedup"] 
        elif x.name == k_p_down.name and x.event_type ==k_p_down.event_type:
            if self.pause==True:
                self.pause =False
            else:
                self.pause=True
            self.key=self.board["pause"]
