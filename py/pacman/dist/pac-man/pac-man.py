import random
import pygame as pg
import time
import keyboard as kb
from method.Button import button as button # cool and useless
import method
from method.img_path import *

# Initialize the game
pg.init() 
# pg.mixer.init()

pg.display.set_caption("pac-man")
# Set up the screen
screen_width = 1000
screen_height = 563
screen = pg.display.set_mode((screen_width, screen_height))
screen_size={"width":1000,"hight":563}

# background

background_image = pg.image.load(imgarr["background"]).convert()
background_image = pg.transform.scale(background_image, (screen_width, screen_height))

tilte = pg.image.load(imgarr["title"]).convert()
tilte = pg.transform.scale(tilte, (int(tilte.get_width()*3.5),int(tilte.get_height()*3.5)))
tilte.set_colorkey(0)

rank_back =pg.image.load(imgarr["rank"]).convert()
rank_back=pg.transform.scale(rank_back,(600,450))
rank_back.set_colorkey(0)

pause_menu2=pg.image.load(imgarr["pause"]).convert()
pause_menu2=pg.transform.scale(pause_menu2, (int(pause_menu2.get_width()*3.5),int(pause_menu2.get_height()*3.5)))
pause_menu2.set_colorkey(0)

icon_img =pg.image.load(imgarr["icon"]).convert()
pg.display.set_icon(icon_img)
# button

exit_image =pg.image.load(buttonarr["exit"]).convert_alpha()
start_image =pg.image.load(buttonarr["start"]).convert_alpha()
rank_image =pg.image.load(buttonarr["rank"]).convert_alpha()
menu_image =pg.image.load(buttonarr["menu"]).convert_alpha()
setting_image=pg.image.load(buttonarr["set"]).convert()
go_on_image=pg.image.load(buttonarr["go"]).convert()
back_img=pg.image.load(buttonarr["back"]).convert()
reset_img=pg.image.load(buttonarr["reset"]).convert()
up_img=pg.image.load(dir_icon["up"]).convert()
right_img=pg.image.load(dir_icon["right"]).convert()
left_img=pg.image.load(dir_icon["left"]).convert()
down_img=pg.image.load(dir_icon["down"]).convert()
pause_img=pg.image.load(dir_icon["pause"]).convert()
speedup_img=pg.image.load(dir_icon["speedup"]).convert()
# sound = pg.mixer.Sound('sound/sound_file.wav')
# sound.play()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
good_look_blue=(202,228,241)

class score_1():
    def __init__(self) :
        self.score=0
    def sub_score(self):
        if self.score >= 100:
            self.score-=100
            return True
        else :
            return False
    def add_score(self,points):
        self.score += points
    def draw_score(self,screen):
        font = pg.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score), True, WHITE)
        screen.blit(score_text, (10, screen_height-50))
class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = YELLOW
        self.radius = 5
        # Create a rect for collision detection
        self.rect = pg.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# class set manage
class game_set():
    def __init__(self):
        self.setfile ={
            "name":"setting",
            "content":0,
            "editTime":0,
            "pubulisher":"Poyenchen",
            "color":"Yellow",
            "lastpaly":"None"
        }
    def set(self):
        # manange all thing to change
        pass
    def draw(self):
        # draw the set draw on game pause and detect any thing i change on setting
        pass

# Create the game objects
# player = Player(0, 0)
player=method.creature.Player(0,0,{"x":45,"y":45},playerarr,5)
ghost1=method.creature.ghost1(400,400,{"x":60,"y":60},ghostarr,1)
ghost2=method.creature.ghost2(200,200,{"x":50,"y":50},ghostarr,1.5)
ghost3=method.creature.ghost1(300,300,{"x":40,"y":40},ghostarr,2)
ghosts = [ghost1,ghost2,ghost3]
ghpos_x=[400,200,300]
ghpos_y=[400,200,300]
pellets = []
score=score_1()
clock = pg.time.Clock()
super_time=0
Kcontroll=method.keyboard.kbcontroller()
FM=method.Filemanage.filemanage()
pickpic=0 # choose which picture of player to use
switch=0
set_game=game_set()
set_bool=False
# other_func
def draw_time(screen, time1):
    font = pg.font.Font(None, 36)
    str1="Time: " + str(round(time1))
    score_text = font.render(str1, True, WHITE)
    screen.blit(score_text, (screen_width/2-len(str1)*9, 10))
    
def draw_text(screen,font,text,size,x,y,color):
    font = pg.font.Font(font, size)
    str1=str(text)
    score_text = font.render(str1, True, color)
    screen.blit(score_text, (x, y))

def randomp(num):
    for i in range(num):
        dx=random.randrange(20, screen_width-20)
        dy=random.randrange(20, screen_height-20)
        pellets.append(Pellet(dx,dy))
randomp(150)

def change_keyboard(key):
    kb.unhook_all()
    kb.on_press(Kcontroll.change)
    Kcontroll.tmp_key=key
    tmp_key=True
    while tmp_key :
        if Kcontroll.change_key:
            tmp_key=False
    Kcontroll.change_key=False
    kb.unhook_all()
    kb.on_press(Kcontroll.lka)
def lagg(t:float):
    t1=time.time()
    t2=time.time()
    while t2-t1<t:
        t2=time.time()
# game function

# menu 
def Menu(running):
    global switch
    c=0
    exit_button =button(890-(exit_image.get_width()*0.5),450,exit_image,1,"exit")
    start_button =button(500-(start_image.get_width()*1.5*0.5),350,start_image,1.5,"start")
    rank_button =button(110-(rank_image.get_width()*0.5),450,rank_image,1,"rank")
    player1=method.creature.player_show(100,250,{"x":70,"y":70},playerarr,2.5)
    ghost_1=method.creature.player_show(0,250,{"x":70,"y":70},ghostarr,2.5)
    player1.direction="right"
    ghost_1.name="ghost"
    while running: 
        clock.tick_busy_loop(60)
        c+=1
        c=c%60
        pc=int((c)/5)%4
        screen.blit(background_image,(0,0))
        screen.blit(tilte,(500-tilte.get_width()*0.5,100))
        player1.move(pc,screen_size)
        ghost_1.move(pc,screen_size)
        player1.draw(screen)
        ghost_1.draw(screen)
        if exit_button.draw(screen):
            #  if exit is true => exit game
            running = False
            switch =2 # switch == 4 => game quit
        if start_button.draw(screen):
            running=False
            switch = 1 # game start
        if rank_button.draw(screen):
            running=False
            switch = 2 # rank start
        # game quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                switch =4 # switch == 4 => game quit
        pg.display.flip()
# main play of game 

def Game_main(running):
    clock.tick_busy_loop(60)
    t1=time.time() #calculate time start
    c=0
    newtime=0
    player=method.creature.Player(0,0,{"x":40,"y":40},playerarr,5)
    global score
    global switch
    global set_bool
    score.score=0
    for i in range(3):
        ghosts[i].x=ghpos_x[i]
        ghosts[i].y=ghpos_y[i]
        ghosts[i].speed=ghosts[i].speed_init
    for pellet in pellets:
        pellets.remove(pellet)
    randomp(150)
    Kcontroll.pause=False
    Kcontroll.pp()
    kb.on_press(Kcontroll.lka)
    lastkey="aa"
    while running and switch !=4:
        clock.tick_busy_loop(60)
        t2=time.time()
        c+=1 
        c=c%60
        level=int((t2-t1-newtime)/2)/10 # it can change the speed of player and ghost
        pickpic=int((c)/5)%4

        # keyboard function
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                # switch == 4 => game quit
                switch =4

        if Kcontroll.key==Kcontroll.board["right"] :
            player.direction = "right"
        if Kcontroll.key==Kcontroll.board["up"]:
            player.direction = "up"
        if Kcontroll.key==Kcontroll.board["down"]:
            player.direction = "down"
        if Kcontroll.key==Kcontroll.board["left"]:
            player.direction = "left"
        if Kcontroll.key==Kcontroll.board["speedup"] and lastkey!=Kcontroll.board["speedup"]:
            tmp_bool=score.sub_score()
            if tmp_bool:
                player.speed+=1
        lastkey=Kcontroll.key

        # user update
        player.move(pickpic,screen_size)

        # Check for collisions between the player and the pellets
        
        for pellet in pellets:
            if player.rect.colliderect(pellet.rect):
                pellets.remove(pellet)
                score.add_score(1)
        if len(pellets)<=250:
            randomp(100)
            
        # Move the ghosts and check for collisions with the player
        for ghost in ghosts:
            ghost.speed=level+ghost.speed_init
            ghost.move(player,pickpic)
            # if player.rect.colliderect(ghost.rect):
            if pg.sprite.collide_mask(player,ghost):
                # switch == 2 => game rank
                switch = 2
                # main game down
                running = False

        # Draw the game objects on the screen
        screen.blit(background_image,(0,0))
        player.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        for pellet in pellets:
            pellet.draw(screen)

        score.draw_score(screen)
        draw_time(screen,t2-t1-newtime)
        pg.display.flip()
        while set_bool ==True or Kcontroll.pause == True :
            if Kcontroll.pause==True and running !=False:
                tnew_1=time.time()
                game_pause(True)
                tnew_2=time.time()
                newtime+=tnew_2-tnew_1

            if set_bool ==True and running !=False:
                buffer=pg.Surface(screen.get_size())
                buffer.blit(screen,(0,0))
                set_function(True,buffer)
                set_bool=False
                Kcontroll.pause=True

                
    kb.unhook_all()
    try:
        FM.winner(round(t2-t1-newtime))
    except:
        FM.cleanwinner()

# game_pause 
def game_pause(pause):
    global set_bool
    global switch
    global screen 
    # build a buffer to store the screen

    buffer=pg.Surface(screen.get_size())
    buffer.blit(screen,(0,0))
    exit_button =button(500-(exit_image.get_width()*0.5),400,exit_image,1,"exit")
    setting_button =button(500-(setting_image.get_width()*0.5),300,setting_image,1,"set")
    continue_button =button(500-(go_on_image.get_width()*0.5),200,go_on_image,1,"go")
    Kcontroll.pp()
    while pause and switch !=4:
        clock.tick_busy_loop(90)
        screen.blit(buffer,(0,0))
        if Kcontroll.pause ==False:
            pause=False
        x=int(screen_width*0.5-pause_menu2.get_width()*0.5)
        y=int(screen_height*0.5-pause_menu2.get_height()*0.5)
        
        screen.blit(pause_menu2,(x,y))
        if setting_button.draw(screen):
            set_bool=True
            pause=False
        if exit_button.draw(screen):
            # game rank exit
            pause = False
            # switch == 4 => game quit
            switch =4
        if continue_button.draw(screen):
            pause = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # game rank down
                pause = False
                # switch == 4 => game quit
                switch =4
        pg.display.flip()
    Kcontroll.pause=False
    Kcontroll.key="aaa"
    screen.blit(buffer,(0,0))
    
def set_function(run,t_img):
    global switch
    global screen 
    up_button =button(260-(up_img.get_width()*0.5),100,up_img,1,"up")
    down_button =button(260-(down_img.get_width()*0.5),200,down_img,1,"down")
    left_button =button(260-(left_img.get_width()*0.5),300,left_img,1,"left")
    right_button =button(260-(right_img.get_width()*0.5),400,right_img,1,"right")
    pause_button =button(620-(pause_img.get_width()*0.5),300,pause_img,1,"pause")
    speedup_button =button(620-(speedup_img.get_width()*0.5),200,speedup_img,1,"speedup")
    reset_button =button(620-(back_img.get_width()*0.5),100,reset_img,1,"reset")
    back_button =button(620-(back_img.get_width()*0.5),400,back_img,1,"back")
    while run and switch !=4:
        clock.tick_busy_loop(90)
        screen.blit(t_img,(0,0))
        screen.blit(rank_back,(500-rank_back.get_width()*0.5,295-rank_back.get_height()*0.5))
        if back_button.draw(screen):
            run =False
            continue
        
        if up_button.draw(screen):
            change_keyboard("up")
        if down_button.draw(screen):
            change_keyboard("down")
        if right_button.draw(screen):
            change_keyboard("right")
        if left_button.draw(screen):
            change_keyboard("left")
        if speedup_button.draw(screen):
            change_keyboard("speedup")
        if pause_button.draw(screen):
            change_keyboard("pause")
        if reset_button.draw(screen):
            Kcontroll.board=FM.board
        draw_text(screen,font_path["retro"],Kcontroll.board["up"],60,310,95,BLACK)
        draw_text(screen,font_path["retro"],Kcontroll.board["down"],60,310,195,BLACK)
        draw_text(screen,font_path["retro"],Kcontroll.board["left"],60,310,295,BLACK)
        draw_text(screen,font_path["retro"],Kcontroll.board["right"],60,310,395,BLACK)
        draw_text(screen,font_path["retro"],Kcontroll.board["speedup"],60,680,195,BLACK)
        draw_text(screen,font_path["retro"],Kcontroll.board["pause"],60,680,295,BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                switch =4
        pg.display.flip()
    screen.blit(t_img,(0,0))
    
# rank
def rank(endgame):
    global switch
    exit_button =button(890-(exit_image.get_width()*0.5),450,exit_image,1,"exit")
    start_button =button(890-(start_image.get_width()*0.5),250,start_image,1,"start")
    menu_button =button(890-(menu_image.get_width()*0.5),350,menu_image,1,"menu")
    reset_button =button(890-(back_img.get_width()*0.5),150,reset_img,1,"reset")
    while endgame  and switch !=4:
        clock.tick_busy_loop(60)
        screen.blit(background_image,(0,0))
        FM.winner_draw(screen,rank_back,None,40)
        if exit_button.draw(screen):
            #  if exit is true => exit game
            endgame = False
            switch =4 # switch == 4 => game quit
        if start_button.draw(screen):
            endgame=False
            switch = 1 # game start
        if menu_button.draw(screen):
            endgame=False
            switch = 0 # menu start
        if reset_button.draw(screen):
            FM.cleanwinner()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                # game rank down
                endgame = False
                # switch == 4 => game quit
                switch =4
        pg.display.flip()
# FM.reset_set()
# game_loop
FM.game_load(Kcontroll,set_game)

run=True   

while(run):
    clock.tick_busy_loop(60)
    if switch==0:
        Menu(True)
    elif switch ==1:    
        Game_main(True)
    elif switch ==2:
        rank(True)
    elif switch ==4:
        # game quit 
        run = False

FM.game_save(Kcontroll,set_game)
