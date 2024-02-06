import random
import json

hello = "Welcome to Po Yen's lottery system\n"
command1 = "add : add a new prize in system"
command2= "get : get a prize"
command3= "end : end the game"
command4= "remv : remove a prize"
command ="there is some command\n"+command1+"\n"+command2+"\n"+command3+"\n"+command4

print(hello)

print(command)

run = True

with open("./price.json", "r") as json_file:
    price_array = json.load(json_file)

while run :
    string1 = input("command : ")
    if string1 == "add":
        string2 = input("what : ")
        price_array.append(string2)
        print(price_array)
    elif string1 =="end":
        run =False
    elif string1 =="get":
        num = len(price_array)
        new = random.randint(0,num-1)
        print (price_array[new])
        price_array.pop(new)
        print(price_array)
    elif string1 =="remv":
        string2 = input("what : ")
        try:
            price_array.remove(string2)
        except:
            print("It is not exisit in array.\nTry again!")
        print(price_array)
    else :
        print("there is something wrong in command\n")
        print(command)

jsonread = open("./price.json",'w')
json.dump(price_array,jsonread,indent=4)
jsonread.close()