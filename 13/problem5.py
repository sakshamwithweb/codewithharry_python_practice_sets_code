# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1,5,9,15,9156,25484,486,1476,78,4,85,4657,8978,6465,646,579]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))