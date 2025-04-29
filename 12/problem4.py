# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the 'ZeroDivisionError'.

try:
    a=1
    b=0
    print(a/b)
except ZeroDivisionError:
    print("infinite")
except Exception as e:
    print("Error")