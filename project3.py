import random
arr = []
def start_player2():
    digit3 = 1
    arr.append(digit3)
    print(arr)
    start_player1()

def chance_computer(num):
    num2 = 4 - num
    while num2 > 0:
        if arr[-1] < 21:
            digit2 = arr[-1] + 1
            arr.append(digit2)
        else:
            print("You lose! Try Next time")
            print("Player1 Wins")
            exit(0)
        num2 -= 1  # Decrement num2 to avoid an infinite loop
    print(arr)
    start_player1()

def check_sequence(num):
    if arr[-1] == 21:
        print("You lose! Try Again Next Time")
        exit(0)
    
    if len(arr) < num:
        return False
    
    for i in range(1, num):
        if arr[-i] - arr[-i-1] != 1:
            print("You Entered an improper sequence")
            return False
        else:
            return True

def start_player1():
    print("How many numbers do you want to insert?")
    num = int(input("-> "))
    if num < 1 or num > 3:
        print("You lose ,You can insert only 3 numbers")
        print("Player 2 Wins!")
        exit(0)
    
    i=1
    while(i<=num):
        digit=int(input("->"))
        arr.append(digit)
        i=i+1
    print(arr)
    value=check_sequence(num)
    if value == False:
        print("You Lose! Try Next Time")
        exit(0)
    else:
        print("Computer's chance\n")
        chance_computer(num)

game = True
while game:
    print("\t\t\tStart Game\n")
    print("Yes/No")
    user = input("-> ")
    if user == "yes" or user == "Yes":
        print("Select Your chance:")
        print("F -> For First chance\nS -> Second Chance")
        chance = input("-> ")
        if chance == "F" or chance == "f":
            start_player1()
        elif chance == "S" or chance == "s":
            start_player2()
        else:
            print("Invalid choice. Exiting game.")
            game = False
    else:
        game = False
