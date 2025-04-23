# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l: # name will have values
    if(name.startswith("S")): # If name startswith S then print hello name
        print(f"Hello {name}")