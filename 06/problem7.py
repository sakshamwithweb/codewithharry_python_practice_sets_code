# Write a program to find out whether a given post is talking about “Harry” or not.

# Taking post from user
post = input("Enter the post: ")

# Checks whether harry or Harry exists in post or not
if("Harry" in post or "harry" in post):
    print("The post talks about Harry!")
else:
    print("The post doesn't talk about Harry")