# redefine all creature of player and ghost ...

# import
import pygame as pg
import math
# from .img_path import *


# class 
class init1(pg.sprite.Sprite):
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        self.size1={
            "x":0,
            "y":0
        }
        self.image=None
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))

    def collide_wall(self):
        if(self.x>1000-self.size1["x"]):
            self.x=1000-self.size1["x"]
        if(self.y>563-self.size1["y"]):
            self.y=563-self.size1["y"]
        if(self.x<0):
            self.x=0
        if(self.y < 0):
            self.y=0


class ghost1(init1):
    def __init__(self,x,y,size,imgarr,speed):
        pg.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.size1=size
        self.imgarr=imgarr
        self.image=pg.image.load(imgarr["preset"]).convert_alpha()
        self.image=pg.transform.scale(self.image,(self.size1["x"],self.size1["y"]))
        self.speed_init=speed
        self.speed=speed
        self.image.set_colorkey(0)
        self.rect = self.image.get_rect()
        self.mask=pg.mask.from_surface(self.image)
    def pic(self,time):
        if time==0:
            self.image =pg.image.load(self.imgarr["g1"]).convert_alpha()
        elif time ==1 or time ==3:
            self.image =pg.image.load(self.imgarr["g2"]).convert_alpha()
        elif time ==2:
            self.image =pg.image.load(self.imgarr["g3"]).convert_alpha()
        self.image=pg.transform.scale(self.image,(self.size1["x"],self.size1["y"]))
        
    def move(self,player,time):
        dx = player.rect.centerx - self.x
        dy = player.rect.centery - self.y
        self.pic(time)
        self.image.set_colorkey(0)
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        self.collide_wall()
class ghost2(ghost1):
    def move(self,player,time):
        dx = player.rect.centerx - self.x
        dy = player.rect.centery - self.y
        dir=player.direction
        if abs(dx)<=100 and abs(dy)<=100:
            pass
        elif dir=="right":
            dx+=100
        elif dir=="left":
            dx-=100
        elif dir=="up":
            dy-=100
        elif dir=="down":
            dy+=100
        self.pic(time)
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        
        
class Player(init1):
    def __init__(self,x,y,size:40,imgarr,speed):
        pg.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.size1=size
        self.imgarr=imgarr
        self.image=pg.image.load(imgarr["preset"]).convert_alpha()
        self.image=pg.transform.scale(self.image,(self.size1["x"],self.size1["y"]))
        self.image.set_colorkey(0)
        self.speed=speed
        self.direction="right"
        self.rect = self.image.get_rect()
        self.mask=pg.mask.from_surface(self.image)
        self.name="player"
    def pic(self,time):
        if self.name!="player":
            if time==0:
                self.image =pg.image.load(self.imgarr["g1"]).convert_alpha()
            elif time ==1 or time ==3:
                self.image =pg.image.load(self.imgarr["g2"]).convert_alpha()
            elif time ==2:
                self.image =pg.image.load(self.imgarr["g3"]).convert_alpha()
        else:
            if self.direction =="right":
                if time==0:
                    self.image = pg.image.load(self.imgarr["close_R"]).convert_alpha()
                elif time==1 or time ==3:
                    self.image = pg.image.load(self.imgarr["1of2_R"]).convert_alpha()
                elif time==2:
                    self.image = pg.image.load(self.imgarr["open_R"]).convert_alpha()
            elif self.direction =="left":
                if time==0:
                    self.image = pg.image.load(self.imgarr["close_L"]).convert_alpha()
                elif time==1 or time ==3:
                    self.image = pg.image.load(self.imgarr["1of2_L"]).convert_alpha()
                elif time==2:
                    self.image = pg.image.load(self.imgarr["open_L"]).convert_alpha()
            elif self.direction =="up":
                if time==0:
                    self.image = pg.image.load(self.imgarr["close_TOP"]).convert_alpha()
                elif time==1 or time ==3:
                    self.image = pg.image.load(self.imgarr["1of2_TOP"]).convert_alpha()
                elif time==2:
                    self.image = pg.image.load(self.imgarr["open_TOP"]).convert_alpha()
            elif self.direction =="down":
                if time==0:
                    self.image = pg.image.load(self.imgarr["close_DOWN"]).convert_alpha()
                elif time==1 or time ==3:
                    self.image = pg.image.load(self.imgarr["1of2_DOWN"]).convert_alpha()
                elif time==2:
                    self.image = pg.image.load(self.imgarr["open_DOWN"]).convert_alpha()
    def move(self,time,screen):
        if self.direction == "right" and self.x <screen["width"]:
            self.x += self.speed
        elif self.direction == "left" and self.x > 0:
            self.x -= self.speed
        elif self.direction == "up" and self.y > 0:
            self.y -= self.speed
        elif self.direction == "down" and self.y < screen["hight"]:
            self.y += self.speed
        self.pic(time)
        self.image = pg.transform.scale(self.image, (self.size1["x"], self.size1["y"]))
        self.collide_wall()
        self.rect.x = round(self.x)  # Update the rect's x-coordinate
        self.rect.y = round(self.y)  # Update the rect's y-coordinate

class player_show(Player):
    def move(self,time,screen):
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left" and self.rect.left > 0:
            self.x -= self.speed
        elif self.direction == "up" and self.rect.top > 0:
            self.y -= self.speed
        elif self.direction == "down" :
            self.y += self.speed
        self.pic(time)
        self.image = pg.transform.scale(self.image,  (self.size1["x"], self.size1["y"]))
        self.collide_with_walls()
        self.rect.x = round(self.x)  # Update the rect's x-coordinate
        self.rect.y = round(self.y)  # Update the rect's y-coordinate
    def collide_with_walls(self):
        if(self.x>=1000):
            self.x=-50