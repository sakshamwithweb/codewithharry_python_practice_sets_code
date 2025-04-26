# Modify the previous program to censor a list of words instead of just one.

censored_words = [
    "Donkey", "donkey",
    "stubborn",
    "kick", "kicked",
    "yell",
    "worse",
    "bray", "brayed",
    "goat", "goats"
]

file = "09/donkey.txt"

with open(file) as f:
    content = f.read()

for i in censored_words:
    content = content.replace(i, "#"*len(i))

with open(file, "w") as newF:
    newF.write(content)