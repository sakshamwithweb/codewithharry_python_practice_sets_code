# Write a program to print the following star pattern.
#   *
#  ***
# *****
# for:

n = int(input("Enter num: "))

for i in range(1, n+1):
    space = ' ' * (n-i)
    stars = (2*i-1) * '*' # 2*i-1 will give the odd number
    print(f"{space}{stars}")