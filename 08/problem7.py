# Write a python function to remove a given word from a list ad strip it at the same time.

l = ["Elon", "Peter", "Mark", "Saksham", "Jeff","Einstein", "APJ", "Ghanshyam", "am"]

# If I want to remove "am" from the list as well as strip it from every value then:
def rem(l,remWord):
    newL = []
    for i in l:
        if(i != remWord):
            newL.append(i.strip(remWord))
    return newL

print(rem(l,"am"))