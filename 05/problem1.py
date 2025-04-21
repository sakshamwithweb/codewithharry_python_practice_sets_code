# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# Dictionary which holds hindi word and its correspond english word
hindi_to_english = {
    "pustak": "book",
    "kutta": "dog",
    "billi": "cat",
    "ghar": "house",
    "khidki": "window",
    "darwaza": "door",
    "pani": "water",
    "aag": "fire",
    "dharti": "earth",
    "aakash": "sky",
    "sooraj": "sun",
    "chaand": "moon",
    "sitara": "star",
    "ped": "tree",
    "phool": "flower",
    "phal": "fruit",
    "nadi": "river",
    "pahaad": "mountain",
    "ladka": "boy",
    "ladki": "girl"
}

# Asking hindi word to user
userInput = input("Write the hindi word: ")

# Output english word of user
print(hindi_to_english[userInput])
