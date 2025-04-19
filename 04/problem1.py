# Write a program to store seven fruits in a list entered by the user.

# Gettint input from user then removing unusual space by strip and replace then convert into list by strip comma
fruits = input("Enter 7 fruits name\n\tSeperated by comma(,)\n\tNo space: ").strip().replace(" ","").split(",")

# Printing the list
print(fruits)