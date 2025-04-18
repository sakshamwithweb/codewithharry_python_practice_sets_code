# Write a python program to display a user entered name followed by Good Afternoon using input () function.


userName = input("What is your name: ")  # Taking userName from user

# Using f string, make the string dynamic, capitalize userName so as to first charwill be capital and rest will be lower
print(f"Good Afternoon {userName.capitalize()}!")
