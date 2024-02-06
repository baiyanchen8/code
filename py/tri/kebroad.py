import keyboard  as kb
import time
import pygame
run=True
# print('a')
class mn():
    def __init__(self) :
        self.a='y'
    def lka(self,x):
        if self.a==x.name:
            return None
        else :
            self.a=x.name
        
        k_up=kb.KeyboardEvent(name='up',scan_code=30,event_type='down')
        k_down=kb.KeyboardEvent(name='down',scan_code=30,event_type='down')
        k_left=kb.KeyboardEvent(name='left',scan_code=30,event_type='down')
        k_rihgt=kb.KeyboardEvent(name='right',scan_code=30,event_type='down')
        k_a=kb.KeyboardEvent(name='a',scan_code=30,event_type='down')
        if x.name==k_up.name and x.event_type==k_up.event_type:
            print("up")
            self.a=x.name
        elif x.name==k_down.name and x.event_type ==k_down.event_type:
            print("down")
            self.a=x.name
        elif x.name==k_left.name and x.event_type ==k_left.event_type:
            print("left")
            self.a=x.name
        elif x.name==k_rihgt.name and x.event_type ==k_rihgt.event_type:
            print("k_rihgt")
            self.a=x.name
        elif x.name ==k_a.name and x.event_type ==k_a.event_type:
            print("a")
            self.a=x.name
clock =pygame.time.Clock()
xy=mn()
while run:
    clock.tick(60)
    
    kb.on_press(xy.lka)
    # 所以可以單獨用個class 處理keyboard & 做分類&&if name==lastname=>不執行