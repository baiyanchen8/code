import json
import datetime

class filemanage():
    def __init__(self):
        self.sett ={
            'name':'setting',
            "content":0,
            "editTime":0,
            "pubulisher":"Poyenchen",
            "setcolor":"y"
        }
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
    def setting(self):
        jsonread = open("./savefile/setting.json",'w')
        json.dump(self.sett,jsonread,indent=4)
        jsonread.close()
        with open("./savefile/setting.json", "r") as json_file:
            data = json.load(json_file)
            # undo need many thing 
        
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
k =filemanage()
k.winner(79)