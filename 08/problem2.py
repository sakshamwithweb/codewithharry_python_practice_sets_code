# Write a python program using function to convert Celsius to Fahrenheit.

# since F = (C * 9/5) + 32

def celToFah(c):
    return c*(9/5) + 32

num = int(input("Enter tempearture in celcius: "))
print(f"{round(celToFah(num), 2)} °F")