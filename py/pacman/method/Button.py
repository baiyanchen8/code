import pygame as pg
import time
button_bool=0
button_time=0
# class button 
class button (): 
    def __init__(self,x,y,image,scale,name):
        self.width=image.get_width()
        self.height=image.get_height()
        self.image=pg.transform.scale(image, (int(self.width*scale), int(self.height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.click=False
        self.x=x
        self.y=y
        self.name=name
    def draw(self,screen):
        global button_bool
        screen.blit(self.image,(self.x,self.y))
        action =False
        mouse_pos=pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]==1 and self.click ==False:
                self.click=True
                action =True
        if pg.mouse.get_pressed()[0]==0:
            self.click=False
        
        if button_bool==True :
            button_bool=False
            return False
        elif action ==True:
            button_bool=True
            return action
        # return what action to take next
        