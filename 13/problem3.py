# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
num = 18
table = [str(x*num) for x in range(1,11)]
print('\n'.join(table))