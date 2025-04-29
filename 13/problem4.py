# Write a program to filter a list of numbers which are divisible by 5.

a = [1,35,1,2,6,5,1,2,5,136,8532,9,79565185,56,5,51684,5,48,2,5,5,2,1458,2,5846]


print(list(filter(lambda x:x%5==0,a)))