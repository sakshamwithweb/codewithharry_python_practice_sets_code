# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

try:
    num: int = int(input("Enter number: "))
    table = [x*num for x in range(1,11)]
    print(table)
except ValueError:
    print("I said numberr")

except Exception as e:
    print("ERRORRRRRRRRRRRRRRRRRR")