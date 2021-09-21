#Finally i have done this
import random
print("Hi, Welcome to the Snake-Water-Gun-Game (-_-)")

while True:
    turns = input("Enter how many tim you want to play?: ")
    if turns.isnumeric():
        turns = int(turns)
        break
    else:
        print("!!Enter Only Number!!")
gamesCount = 0
pcw = 0
usw = 0
lst = ("S", "W", "G")

while turns > 0:
    gamesCount += 1
    pcc = random.choice(lst)
    while True:
        print(f"Games No. {gamesCount}")
        print("'S' for 'Snake'\n'W' for 'Water'\n'G' for Gun")
        usc = (input("Choose yours: "))
        if usc.upper() in lst:
            break
        else:
            print("Invalid Input")
    if usc.upper() == 'S':
        if pcc == 'W':
            usw = usw + 1
            print("You have choosed Snake and Computer Choosed Water")
            print("Snake drank Water!!")
            print("You won and Computer lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        elif  pcc == "G":
            pcw = pcw + 1
            print("You have choosed Snake and Computer choosed Gun")
            print("Snake got shooted by Gun!!")
            print("Computer won and You lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        else:
            print("You have choosed Snake and Computer choosed Snake")
            print("Match Tied!!, No one wins")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
    elif usc.upper() == 'W':
        if pcc == 'G':
            usw = usw + 1
            print("You have choosed Water and Computer Choosed Gun")
            print("Gun drowned in Water!!")
            print("You won and Computer lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        elif pcc == 'S':
            pcw = pcw + 1
            print("You have choosed Water and Computer choosed Snake")
            print("Snake drank Water!!")
            print("Computer won and You lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        else:
            print("You have choosed Water and Computer choosed Water")
            print("Match Tied!!, No one wins")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
    elif usc.upper() == 'G':
        if pcc == 'S':
            usw = usw + 1
            print("You have choosed Gun and Computer choosed Snake")
            print("Snake got shooted by Gun!!")
            print("You won and Computer lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        elif pcc == 'W':
            pcw = pcw + 1
            print("You have choosed Gun and Computer choosed Water")
            print("Gun drowned in Water!!")
            print("Computer won and You lost")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
        else:
            print("You have choosed Gun and Computer choosed Gun")
            print("Match Tied!!, No one wins")
            print(f"Current Score:\nYour Wins: {[usw]}\nComputer Wins: {[pcw]}")
    else:
        print("!!Something went Wrong!!")
    turns -= 1
    if (turns == 0):
        print("#####Final Result#####")
        print(f"Final Score:\nYour Score: {[usw]}\nComputer Score: {[pcw]}")
        if usw > pcw:
            print("!!You Won!!")
        elif pcw > usw:
            print("!!Computer Won!!")
        else:
            print("!!Match Tied!!")
    
        while True:
            playAgain = input("\nDo you want to play again? (Y/N): ")
            if playAgain.upper() == "Y":
                turns = int(input("\nHow many games do you want to play?: "))
                gamesCount = 0
                usw = 0
                pcw = 0
                break
            elif playAgain.upper() == "N":
                print("Thanks for playing...!!!")
                break
            else:
                print("Value should be either Y or N. Try again...!!!")
                continue
    continue
