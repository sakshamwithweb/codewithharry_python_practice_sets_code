# Write a program to replace every occurrence of the word 'Donkey' in a file with '#####' and update the same file.

file = "09/donkey.txt"

with open(file) as f:
    content = f.read()
    
    updated_content = content.replace("Donkey","#####").replace("donkey",'#####')

    with open(file,"w") as newF:
        newF.write(updated_content)

print("Done!")