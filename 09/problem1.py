# Write a program to read the text from a file 'poems.txt' and check whether it contains the word 'twinkle'.

word= 'twinkle'

with open("09\poem.txt","r") as f:
    poems = f.read()
    if(word in poems):
        print(f"{word} exists in poems")
    else:
        print(f"Word: {word} doesn't exist")