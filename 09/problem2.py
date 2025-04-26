# Write a program to read a file 'Hi-score.txt' and update the Hi-score if the current score returned by the game() function is higher.

import random
import time

score = 0

# This function will create Hi-score.txt(if doesn't exist) and update the score
def updateFile(score):
    with open("09/Hi-score.txt", "w") as f:
        f.write(str(score))

# This function will call updateFile in beginning to create then using random.choice, will pretend the score whether it is draw or +1 and update the file and will call itself after every 2 seconds.
def game(score):
    updateFile(score)

    possibilities = [0, 1]
    message = {
        1: "You won!",
        0: "Draw!!",
        -1: "You lose1"
    }
    decision = random.choice(possibilities)
    print(message[decision])

    if (decision != 0):
        score += 1
        updateFile(score)
    time.sleep(2)
    game(score)

game(score)