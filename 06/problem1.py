# Write a program to find the greatest of four numbers entered by the user.

# Getting n1, n2, n3 and n4
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))

# Checking if n_ numbe ris bigger than others, if yes, print or else, next.
if (n1 > n2 and n1 > n3 and n1 > n4):
    print(f"Biggest Number is {n1}")
elif (n2 > n1 and n2 > n3 and n2 > n4):
    print(f"Biggest Number is {n2}")
elif (n3 > n1 and n3 > n2 and n3 > n4):
    print(f"Biggest Number is {n3}")
else:
    print(f"Biggest Number is {n4}")
