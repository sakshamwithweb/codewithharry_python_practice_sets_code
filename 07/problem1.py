# Write a program to print multiplication table of a given number using for loop

num = int(input("Enter number: ")) # Input the number

for i in range(1, 11): # Using a for loop which starts from 1 till 10
    print(f"{num}X{i} = {i*num}") # It will print i(1 to 10) * num