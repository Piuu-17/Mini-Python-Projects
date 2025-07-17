import random
target=random.randint(1,10)
while True:
    userChoice=int(input("enter your choice:"))
    if (userChoice==target):
        print("CONGRATULATIONS!! correct guess")
        break
    elif(userChoice<target):
        print("OOPS!Enter a bigger choice") 
    else:
        print("OOPS!Enter a smaller choice")

print("-----GAME OVER-----")


    

