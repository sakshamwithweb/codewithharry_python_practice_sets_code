# Write a recursive function to calculate the sum of first n natural numbers

'''
f(6) = 6 + 5 + 4 + 3 + 2 + 1
f(5) = 5 + 4 + 3 + 2 + 1
f(4) = 4 + 3 + 2 + 1
f(3) = 3 + 2 + 1
f(2) = 2 + 1
f(1) = 1

f(n) = n + (n-1) + .... 2 + 1
f(n) = n + f(n-1)
'''

# Same as factorial but just use + instaed of *


def NaturalNumSum(n):
    if (n == 1):
        return n
    return NaturalNumSum(n-1) + n  # recursion


num = int(input("Enter Number: "))

print(NaturalNumSum(num))
