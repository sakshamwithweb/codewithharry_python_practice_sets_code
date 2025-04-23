# Write a program to find the sum of first n natural numbers using while loop.

num = int(input("Enter first natural numbers quantity: ")) # Taking input from user

sum = 0 # it will store the sum

i = 1 # it is natural numer, starts form 1
while i <= num: # firstly i will be 1 then 2.... till the last natural number user typed
    sum += i # adding the current natural number in sum
    i += 1

print(sum)