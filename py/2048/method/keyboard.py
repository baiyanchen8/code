import keyboard as kb
from . import map
class kbcontroller():
    def __init__(self) :
        self.key="aaa"
        self.mapping=map.class_map()
        self.pause=False
        self.tmp_key=""
        self.change_key=False
        self.list=["up","down","left","right"]
        self.board={
            "up":"up",
            "down":"down",
            "left":"left",
            "right":"right",
        }
    def lka(self,x):
        
        if x.event_type =='down':
            return

        print(x)
        self.mapping.push_button(x.name)
       