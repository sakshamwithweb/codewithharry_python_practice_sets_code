# Write a program to find whether a given username contains less than 10 characters or not.

userName = input("Enter userName: ") # Input userName

if(len(userName)<10): # If username length is less than 10:
    print("Contains less than 10 characters.")
else:
    print("Conatins more than 10 characters")