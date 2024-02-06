import json
import datetime
import pygame as pg
class filemanage():
    def __init__(self):
        self.setfile ={
            "name":"setting",
            "content":0,
            "editTime":0,
            "pubulisher":"Poyenchen",
            "color":"Yellow",
            "lastpaly":"None"
        }
        self.set_List=["name","content","editTime","publisher","color","lastplay"]
        self.jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
        self.win={
            "1":0,"2":0,"3":0,"4":0,"5":0,
            "6":0,"7":0,"8":0,"9":0,"10":0
        }
        self.list_file=["1","2","3","4","5","6","7","8","9","10"]
        self.win_time={
            "1":"None","2":"None","3":"None","4":"None","5":"None",
            "6":"None","7":"None","8":"None","9":"None","10":"None"
        }
        self.board={
            "up":"up",
            "down":"down",
            "left":"left",
            "right":"right",
            "speedup":"a",
            "pause":"p"
        }
    def game_load(self,kb,st):
        with open("./savefile/setting.json", "r") as json_file:
            data = json.load(json_file)
        with open("./savefile/kb.json", "r") as json_file:
            data = json.load(json_file)
        kb.board=data
    def game_save(self,kb,st):
        self.board=kb.board
        jsonread = open("./savefile/kb.json",'w')
        json.dump(self.board,jsonread,indent=4)
        jsonread.close()
        self.setfile=st.setfile
        jsonread = open("./savefile/setting.json",'w')
        json.dump(self.setfile,jsonread,indent=4)
        jsonread.close()
    def reset_set(self):
        jsonread = open("./savefile/setting.json",'w')
        json.dump(self.setfile,jsonread,indent=4)
        jsonread.close()
        jsonread = open("./savefile/kb.json",'w')
        json.dump(self.board,jsonread,indent=4)
        jsonread.close()
        jsonread = open("./savefile/winner.json",'w')
        json.dump(self.win,jsonread,indent=4)
        jsonread.close()
        jsonread = open("./savefile/winner_time.json",'w')
        json.dump(self.win,jsonread,indent=4)
        jsonread.close()
    def cleanwinner(self):
        jsonread = open("./savefile/winner.json",'w')
        json.dump(self.win,jsonread,indent=4)
        jsonread.close()
        jsonread = open("./savefile/winner_time.json",'w')
        json.dump(self.win,jsonread,indent=4)
        jsonread.close()
    def winner(self,time):
        with open("./savefile/winner.json", "r") as json_file:
            winner_Time = json.load(json_file)
        with open("./savefile/winner_time.json", "r") as json_file:
            winner_Date = json.load(json_file)
        today=datetime.date.today()
        k=str(today)
        for i in range(10):
            if winner_Time[self.list_file[i]] <=time:
                tmp=winner_Time[self.list_file[i]]
                tmp2=winner_Date[self.list_file[i]]
                winner_Time[self.list_file[i]]=time
                winner_Date[self.list_file[i]]=k
                time=tmp
                k=tmp2
        jsonread = open("./savefile/winner.json",'w')
        json.dump(winner_Time,jsonread,indent=4)
        jsonread.close()
        jsonread = open("./savefile/winner_time.json",'w')
        json.dump(winner_Date,jsonread,indent=4)
        jsonread.close()
    def draw_place(self,screen,num,x,y,time,date,font,size):
        font = pg.font.Font(font, size)
        str1=str(num)+":" + str(time)+" "+str(date)
        score_text = font.render(str1, True, (0,0,0))
        screen.blit(score_text, (x, y))
    def winner_draw(self,screen,rank_back,font,size):
        with open("./savefile/winner.json", "r") as json_file:
            winner_Time = json.load(json_file)
        with open("./savefile/winner_time.json", "r") as json_file:
            winner_Date = json.load(json_file)
        
        screen.blit(rank_back,(200,60))
        x=0
        y=60
        for i in range(10):
            time=winner_Time[self.list_file[i]]
            date=winner_Date[self.list_file[i]]
            if i<5:
                x=235
            elif i==5:
                y=60
                x=535
            y+=75
            self.draw_place(screen,i+1,x,y,time,date,font,size)