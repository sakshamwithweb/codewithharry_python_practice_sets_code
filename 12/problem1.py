# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open("12/1.txt","r") as f1:
        print(f1.read())
except:
    print("Error in 1")


try:
    with open("12/2.txt","r") as f2:
        print(f2.read())
except:
    print("Error in 2")


try:
    with open("12/3.txt","r") as f3:
        print(f3.read())
except:
    print("Error in 3")
