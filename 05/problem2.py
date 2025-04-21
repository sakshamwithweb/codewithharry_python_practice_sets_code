# Write a program to input eight numbers from the user and display all the unique numbers (once).

#  Defining a set
numbers = set()

# Asking 8 numbers and converting to integer then appending in the set
int1 = int(input("Enter 1st Number: "))
numbers.add(int1)
int2 = int(input("Enter 2nd Number: "))
numbers.add(int2)
int3 = int(input("Enter 3rd Number: "))
numbers.add(int3)
int4 = int(input("Enter 4th Number: "))
numbers.add(int4)
int5 = int(input("Enter 5th Number: "))
numbers.add(int5)
int6 = int(input("Enter 6th Number: "))
numbers.add(int6)
int7 = int(input("Enter 7th Number: "))
numbers.add(int7)
int8 = int(input("Enter 8th Number: "))
numbers.add(int8)

# Prining the unique values
print(f"Unique values are: {numbers}")
