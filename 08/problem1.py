# Write a program using functions to find greatest of three numbers.

def greatestOfThree(n1, n2, n3):
    nums = [n1, n2, n3]
    nums.sort()
    nums.reverse()
    return nums[0]


n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

print(f"Greatest of three is: {greatestOfThree(n1, n2, n3)}")
