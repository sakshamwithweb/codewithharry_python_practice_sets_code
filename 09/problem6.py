# Write a program to read a log file and check whether it contains the word 'python'.

with open("09/.log") as log:
    logs = log.read()
    print('python' in logs.lower())