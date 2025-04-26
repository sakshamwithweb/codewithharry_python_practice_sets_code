# Write a program to wipe out (clear) the contents of a file.

file = "09/file.txt"

with open(file,"w") as f:
    f.write("")

print("cleared")