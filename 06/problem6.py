# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

mark = int(input("Enter your percentage: ")) # Taking marks from user

# Checking where does user's number lie
if(mark>=90 and mark<=100):
    print("Ex")

elif(mark>=80 and mark<=90):
    print("A")

elif(mark>=70 and mark<=80):
    print("B")

elif(mark>=60 and mark<=70):
    print("C")

elif(mark>=50 and mark<=60):
    print("D")

else:
    print("F")