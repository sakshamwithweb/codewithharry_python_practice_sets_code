'''
Write a python function to print first n lines of the following pattern:
***
** 
*

for - n = 3

'''

def createStarPattern(n):
    if(n==1):
        print("*")
        return
    print("*"*n)
    createStarPattern(n-1)

num = int(input("Enter Number: "))

createStarPattern(num)