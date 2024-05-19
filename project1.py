import random
from numpy import *
num=random.randint(1,100)
a=1
while(log2(100-1+1)):
    digit=int(input("Enter correct number :"))
    if(digit == num):
        print("Winner! You Guessed Correct number")
        break
    elif(digit < num):
        print("The Value You entered is less than the correct value,Try Again!")
    elif(digit > num):
        print("The Value You entered is greater than the correct value,Try Again!")
    a=a+1
print("Total number of guess=",a)
  
