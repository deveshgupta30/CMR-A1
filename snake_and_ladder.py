import random
print("Welcome to the classic Snake and Ladder Game!!!")
print("Terms & Conditions: \nPlease agree to the T&C given below:")
t=input("* This is a Single Player Game! \n*The game is easy to play. \n*Good Luck from the coder! :) \nDo you agree? \n'yes' to continue:")
dice=0
score=0
score1=0
roll=0
dice1=0
if t=='yes':
    while score<=100:
        roll=int(input("\nPress 1 to roll: "))
        if roll==1:
            dice=random.randint(1,6)
            score=score+dice
            print("Your dice rolled to:",dice,"\nYou are in position:",score)
            if score==8:
                score=37
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==11:
                score=2
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==13:
                score=34
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==25:
                score=4
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==38:
                score=9
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==40:
                score=68
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==52:
                score=81
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==65:
                score=46
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==76:
                score=97
                print("Oh Great! You got the ladder! :D You go to:",score)
            if score==89:
                score=70
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==93:
                score=64
                print("Oh No! A snake bit you! :( You fall back to:",score)
            if score==100:
                print("Congratulations! You won!!!")
                break
            if score>=100:
                score=score-dice
                if score==95:
                    if dice==6:
                        print("Can't move.")
                if score==96:
                    if (dice==6) or (dice==5):
                        print("Can't move.")
                if score==97:
                    if (dice==6) or (dice==5) or (dice==4):
                        print("Can't move.")
                if score==98:
                    if (dice==6) or (dice==5) or (dice==4) or (dice==3):
                        print("Can't move.")
                if score==99:
                    if (dice==6) or (dice==5) or (dice==4) or (dice==3) or (dice==2):
                        print("Can't move.")
        else:
            break
