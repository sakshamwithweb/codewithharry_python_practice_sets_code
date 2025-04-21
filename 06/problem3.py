# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
# Write a program to detect these spams.

# List of all spam keywords
spamKeywords=["Make a lot of money", "buy now", "subscribe this", "click this"]

# Comment from user
comment = input("Enter comment: ")

# Checking whether any keyword matches, before checking converting to lower case due to case sensiteveness
if((spamKeywords[0] in comment) or (spamKeywords[1] in comment) or (spamKeywords[2] in comment) or (spamKeywords[3] in comment)):
    print("Given comment contains spam keywords")
else:
    print("Uploaded!")