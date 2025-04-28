'''
~~~~~~~~~~~~~~~~~~PROJECT 2 :- THE PERFECT GUESS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are going to write a program that generates a random number and asks the user to guess it. If the player's guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user's guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number. 

Hint: Use the random module.
'''

import random


attempts = 0

def ask_and_check(actualNum,attempts):
    attempts += 1
    userNum = int(input("Enter number: "))
    if(userNum<1 or userNum>100):
        print("Enter between 1 and 100..")
    elif(userNum>actualNum):
        print("Lower number please")
    elif(userNum<actualNum):
        print("Higher number please")
    else:
        print(f"Won || Attempts: {attempts}")
        return
    ask_and_check(actualNum,attempts)

def start():
    actualNum = random.randint(1,100)
    ask_and_check(actualNum,attempts)

start()