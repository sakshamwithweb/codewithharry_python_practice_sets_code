# Write a python function which converts inches to cms.
# 1 Inch = 3.5 cm

def inchToCm(n):
    if (num <= 0):
        return "Invalid measurement"
    elif (num == 1):
        return "Why did you born as a human???"
    else:
        return f"{num} Inches = {round(n*2.54,2)}"


print("1 Inch = 2.54 cm", end="\n")
num = int(input("Enter Number: "))

print(inchToCm(num))