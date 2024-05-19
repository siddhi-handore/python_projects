import random
names=["books","pencil","pen","games","LunchBox","uniform","teacher","principle","time","friends","bag"]
item=random.choice(names)
num=5
chance=1
while(chance <= num):
    data=input("Enter any Random item Related to school:")
    if(item == data):
        print("You won!,Guessed correct Object")
        break
    else:
        print(chance+1,"chance")
        print("Try Again")
    chance+=1


