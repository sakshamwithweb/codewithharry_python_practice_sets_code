# Write a program to find whether a given number is prime or not.

num = int(input("Enter the number: "))  # Getting number

for i in range(2, num-1):  # Starts from 2 and ends at num-1 because prime number can be devided by 1 and itself
    if (num % i == 0):  # if num devides by i and give 0 as remainder then...
        print(f"{num} is not a prime number, as it is divisible by {i}")
        break
else:  # If no number was able to devide then...
    print(f"{num} is a prime number")
