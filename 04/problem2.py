# Write a program to accept marks of 6 students and display them in a sorted manner.

# Define a list named marks
marks = []

# Asking marks of each students, converting to integer and appending in list 'marks'. 
s1 = int(input("Enter 1st student marks(only number): "))
marks.append(s1)
s2 = int(input("Enter 2nd student marks(only number): "))
marks.append(s2)
s3 = int(input("Enter 3rd student marks(only number): "))
marks.append(s3)
s4 = int(input("Enter 4th student marks(only number): "))
marks.append(s4)
s5 = int(input("Enter 5th student marks(only number): "))
marks.append(s5)
s6 = int(input("Enter 6th student marks(only number): "))
marks.append(s6)

# Sorting the final list in ascending order
marks.sort()

# Using f string and printing
print(f"List of sorted marks is: {marks}")