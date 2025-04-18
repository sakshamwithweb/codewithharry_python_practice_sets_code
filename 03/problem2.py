# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''


# Sharing bit more info ; )
print("You are choosen as the best contributer and we are happy ton invite you in CEO sit.")
print("Please fill all information true to avoid any future delay..")

# User name and capitalizing it
name = input("Write your name please: ").capitalize()

date = input("Write today's date in DD/MM/YYYY formate: ")  # Today's date

# Using f string
print(f"Here is your letter:\n\nDear {name},\nYou are selected!\n{date}\n\n\n")
