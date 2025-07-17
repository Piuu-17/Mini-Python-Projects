#stone=1 , paper=-1 , scissor=0

import random
 
computer=random.choice(1,-1,0)
you=int(input("enter your choice:"))
# myDict={"s":1 , "p":-1 ,"sci":0}
# reverseDic={1:"s",-1:"p",0:"sci"}
# you=myDict[youstr]
# print(f"YOU CHOSE{reverseDic[you]} \n COMPUTER CHOSE{reverseDic[computer]}


if(computer==you):
    print("DRAW")
elif(computer==1 and you==-1):
    print("YOU WIN")
    
elif(computer==1 and you==0):
    print("COMPUTER WINS")
    
elif(computer==-1 and you==1):
    print("COMPUTER WINS")
    
elif(computer==-1 and you==0):
    print("YOU WIN")
    
elif(computer==0 and you==1):
    print("YOU WIN")
    
elif(computer==0 and you==-1):
    print("COMPUTER WINS")
    
else:
    print("OOPS something went wrong")




  