# Attempt problem 1 using while loop.

# Write a program to print multiplication table of a given number using while loop

num = int(input("Enter number: "))  # Input the number

i = 1  # declaring i
while i <= 10:  # If i is less or equal than 10
    print(f"{num}X{i} = {i*num}")  # print i*num
    i += 1
