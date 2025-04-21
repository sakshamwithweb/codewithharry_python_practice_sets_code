# Write a program which finds out whether a given name is present in a list or not.

# Defining list
l=["Saksham","Bill","Elon","Jeff","Sundar","Ratan","Harish","Universe","Mark","George","Peter","Warren"]

# Get user name
name = input("Enter your name: ")

# Checking whether user name exists or not
if(name in l):
    print("You deserve this life!")
else:
    print("You could deserve your life if you work hard")