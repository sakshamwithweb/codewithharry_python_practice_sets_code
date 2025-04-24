# PROJECT 1: ROCK, PAPER, SCISSOR GAME
import random

possibilities = ["rock", "paper", "scissor"]

def getWinner(userChoice, botChoice):
    if (userChoice == botChoice):
        return "Draw!"
    elif (userChoice == "rock" and botChoice == "scissor"):
        return "User won!"
    elif (userChoice == "paper" and botChoice == "rock"):
        return "User won!"
    elif (userChoice == "scissor" and botChoice == "paper"):
        return "User won!"
    else:
        return "Bot won!"


def play():
    userChoice = input("Enter choice (rock, paper, scissor): ").lower()
    botChoice = random.choice(possibilities)
    if (userChoice in possibilities):
        print(f"You chose: {userChoice}")
        print(f"Bot chose: {botChoice}")
        print(getWinner(userChoice,botChoice))
        print("~"*80)
        play()
    else:
        print("Invalid input! Try again")
        play()

play()
