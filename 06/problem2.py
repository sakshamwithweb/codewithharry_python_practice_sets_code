# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

subjectMarks = {}  # Declaring a dictionary to store subject and its marks

# Asking subjects and correspond marks
s = input("Enter Subject Name: ")
m = int(input(f"Enter marks you got in {s}: "))
subjectMarks.update({s: m})
s = input("Enter Subject Name: ")
m = int(input(f"Enter marks you got in {s}: "))
subjectMarks.update({s: m})
s = input("Enter Subject Name: ")
m = int(input(f"Enter marks you got in {s}: "))
subjectMarks.update({s: m})

# .keys returns all keys in dict_keys named data type and then we are converting to list
listOfSubjects = list(subjectMarks.keys())

# Getting marks of subject1,2 and 3
subject1=subjectMarks[listOfSubjects[0]]
subject2=subjectMarks[listOfSubjects[1]]
subject3=subjectMarks[listOfSubjects[2]]

# Total percentage
totalPercentage= round(((subject1+subject2+subject3)/300)*100 , 2)

# Conditional if everysubjectgot minimum 33% and total is 40 % then goo
if(subject1 >= 33 and subject2 >= 33 and subject3 >= 33) and totalPercentage>=40:
    print(f"Cangratulation! Your are passed!\n\nYour percentage: {totalPercentage}")
else:
    print(f"Cangratulation! You got chance to study this session again ⊙﹏⊙∥\n\nYour percentage: {totalPercentage}%")