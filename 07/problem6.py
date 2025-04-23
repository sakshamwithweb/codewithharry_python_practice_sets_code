# Write a program to calculate the factorial of a given number using for loop.

# factorial of 5: 1*2*3*4*5 = 120

num = int(input("Enter number: "))  # Taking input from user

product = 1 # It will be the total porduct or factorial, start from 1, if starts from 0, it will eat all ands make 0

for i in range(1, num+1): # Start for loop from 1 to num+1 means number itself as end = n-1
    product *= i # Multiplying the current i with product

print(product)