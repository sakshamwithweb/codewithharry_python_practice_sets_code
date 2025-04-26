# Write a program to make a copy of a text file named 'this.txt'.

with open("09/this.txt") as f:
    content = f.read()

with open("09/copy_this.txt","w") as cf:
    cf.write(content)