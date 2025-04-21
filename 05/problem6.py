# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dic = {}  # Craeting an empty dictionary

# Asking name and fav lang and updateing the dic
name = input("Bro 1, enter your name: ")
favLang = input("Bro 1, enter your favourite Programming Language: ")
dic.update({name: favLang})

name = input("Bro 2, enter your name: ")
favLang = input("Bro 2, enter your favourite Programming Language: ")
dic.update({name: favLang})

name = input("Bro 3, enter your name: ")
favLang = input("Bro 3, enter your favourite Programming Language: ")
dic.update({name: favLang})

name = input("Bro 4, enter your name: ")
favLang = input("Bro 4, enter your favourite Programming Language: ")
dic.update({name: favLang})


print(dic)  # Printing the final dic
