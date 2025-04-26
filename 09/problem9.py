# Write a program to check whether two text files have identical content.

with open("09/this.txt") as f:
    content = f.read()

with open("09/copy_this.txt") as cf:
    copy_content = cf.read()

if(content==copy_content):
    print("Yup! Files are identical")
else:
    print("No! Files are not identical")