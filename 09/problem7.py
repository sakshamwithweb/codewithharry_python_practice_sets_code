# Write a program to find and print the line numbers in a file where the word 'python' appears.

with open("09/.log") as log:
    logs = log.readlines()

for line in logs:
    if ('python' in line.lower()):
        print(f"'python' word is in line: {logs.index(line)+1}")
        break
else:
    print("No line contains 'python' word")
