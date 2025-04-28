import random

attempts = 0
actualNum = random.randint(1,100)
userNum=0
while(actualNum!=userNum):
    userNum = int(input("Enter number: "))
    if(actualNum>userNum):
        print("Higher number please")
    elif(actualNum<userNum):
        print("Lower number please")
    attempts += 1

print(f"Won, No. of Attempts:{attempts}")