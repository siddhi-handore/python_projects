import random
choices=["Rock","Paper","Scissor"]
def check(user,comp):
    if(user==comp):
        print(f"Player=>{user}\t Computer=>{comp}\n")
        print("Retry!,You both got same values\n")
    elif((user=="Rock" and comp=="Scissor") or (user=="Paper" and comp=="Rock") or (user=="Scissor" and comp=="Paper")):
        print(f"Player=>{user}\t Computer=>{comp}\n")
        print("Congratulations,You won")
    else:
        print(f"Player=>{user}\t Computer=>{comp}\n")
        print("Ohh! You Lose,Computer Wins")

def start_game():
    while True:
        user=input("Enter your Element:")
        user=user.capitalize()
        if(user == "R"):
            user="Rock"
            break
        elif(user == "P"):
            user="Paper"
            break
        elif(user =="S"):
            user="Scissor"
            break
        else:
            print("You Entered incorrect vlaue")
            
    comp=random.choice(choices)
    check(user,comp)

game=True
while game:
    print("\t\t\tStart Game\n(Say Yes/No)")
    ans=input("->")
    if ans=="Yes" or ans=="yes":
        print("R->Rock\nP->Paper\nS->Scissor\n")
        start_game()
        play=True
        while play:
            print("Play More\n(Say Yes/No)")
            user_choice=input("->")
            user_choice=user_choice.capitalize()
            if(user_choice == "Yes"):
                start_game()
            else:
                print("Game Over")
                play=False
                game=False
    else:
        game=False
        