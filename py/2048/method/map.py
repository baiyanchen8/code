import pygame as pg
import random
from . import color
from . import text
class class_map:
    def __init__(self):
        self.mmap=[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        # (x,y)
        # size =100*100
        # space =20
        self.position=[
            [[20,20] ,[140,20] ,[260,20] ,[380,20]] ,
            [[20,140],[140,140],[260,140],[380,140]],
            [[20,260],[140,260],[260,260],[380,260]],
            [[20,380],[140,380],[260,380],[380,380]]    
        ]
        random_x = random.randint(0, 3)
        random_y = random.randint(0, 3)
        if self.mmap[random_x][random_y]==0:
            random_int=random.randint(0,1)
            if random_int==0:
                self.mmap[random_x][random_y]=2
            else:
                self.mmap[random_x][random_y]=4
    def draw(self,screen):
        for i in range(4):
            for j in range(4):
                now=self.position[i][j]
                num=self.mmap[i][j]
                block_rect = pg.Rect(now[0], now[1], 100, 100)
                pg.draw.rect(screen, color.orange, block_rect)
                if num!=0:
                    text.draw_text(screen,num,36,now[0],now[1],color.BLACK)
    def push_button(self,key):
        if key =='up':
            self.up()
        if key =='down':
            self.down()
        if key =='left':
            self.left()
        if key =='right':
            self.right()
        running=True
        while (running):
            random_x = random.randint(0, 3)
            random_y = random.randint(0, 3)
            if self.mmap[random_x][random_y]==0:
                random_int=random.randint(0,1)
                if random_int==0:
                    self.mmap[random_x][random_y]=2
                else:
                    self.mmap[random_x][random_y]=4
                running=False
    def up(self):
        priority =[1,2,3]
        for y in priority:
            for x in range(4):
                for y1 in range(y):
                    now = self.mmap[y-y1][x]
                    up=self.mmap[y-1-y1][x]
                    if  now!=0 :
                        if up==0:
                            self.mmap[y-1-y1][x]=now
                            self.mmap[y-y1][x]=0
        for y in priority:
            for x in range(4):
                now = self.mmap[y][x]
                up=self.mmap[y-1][x]
                if now == 0:
                    continue
                if  now!=0 :
                    if up==0:
                        self.mmap[y-1][x]=now
                        self.mmap[y][x]=0
                    elif up==now:
                        self.mmap[y-1][x]=self.mmap[y-1][x]*2
                        self.mmap[y][x]=0
        for y in priority:
            for x in range(4):
                for y1 in range(y):
                    now = self.mmap[y-y1][x]
                    up=self.mmap[y-1-y1][x]
                    if  now!=0 :
                        if up==0:
                            self.mmap[y-1-y1][x]=now
                            self.mmap[y-y1][x]=0
        
    def down(self):
        priority =[2,1,0]
        for y in priority:
            for x in range(4):
                for y1 in range(3-y):
                    now = self.mmap[y+y1][x]
                    down=self.mmap[y+1+y1][x]
                    if  now!=0 :
                        if down==0:
                            self.mmap[y+1+y1][x]=now
                            self.mmap[y+y1][x]=0
        for y in priority:
            for x in range(4):
                now = self.mmap[y][x]
                down=self.mmap[y+1][x]
                if  now!=0 :
                    if down==0:
                        self.mmap[y+1][x]=now
                        self.mmap[y][x]=0
                    elif down==now:
                        self.mmap[y+1][x]=self.mmap[y+1][x]*2
                        self.mmap[y][x]=0
        for y in priority:
            for x in range(4):
                for y1 in range(3-y):
                    now = self.mmap[y+y1][x]
                    down=self.mmap[y+1+y1][x]
                    if  now!=0 :
                        if down==0:
                            self.mmap[y+1+y1][x]=now
                            self.mmap[y+y1][x]=0
    def left(self):
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                x1=x
                while x1 > 0 :
                    left=  self.mmap[y][x1-1]
                    if left == 0:
                        self.mmap[y][x1-1]=self.mmap[y][x1]
                        self.mmap[y][x1]=0
                    x1-=1
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                now = self.mmap[y][x]
                left=  self.mmap[y][x-1]
                if left == now:
                    self.mmap[y][x-1]=2*now
                    self.mmap[y][x]=0
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                x1=x
                while x1 > 0 :
                    left=  self.mmap[y][x1-1]
                    if left == 0:
                        self.mmap[y][x1-1]=self.mmap[y][x1]
                        self.mmap[y][x1]=0
                    x1-=1     
    def right(self):
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                x1=x
                while x1 > 0 :
                    right=  self.mmap[y][x1+1]
                    if right == 0:
                        self.mmap[y][x1+1]=self.mmap[y][x1]
                        self.mmap[y][x1]=0
                    x1-=1
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                now = self.mmap[y][x]
                right=  self.mmap[y][x+1]
                if right == now:
                    self.mmap[y][x+1]=2*now
                    self.mmap[y][x]=0
        for x in [1,2,3]:
            for y in [0,1,2,3]:
                x1=x
                while x1 > 0 :
                    right=  self.mmap[y][x1+1]
                    if right == 0:
                        self.mmap[y][x1+1]=self.mmap[y][x1]
                        self.mmap[y][x1]=0
                    x1-=1