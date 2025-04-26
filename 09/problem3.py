# Write a program to generate multiplication tables from 2 to 20 and write each to a different file. Save these files in a folder named appropriately for a 13-year-old.
import os

# This will generate table of n
def generateTable(n):
    a=[]
    for i in range(1,11):
        a.append(f"{n} X {i} = {n*i}")
    return "\n".join(a)

# This is main function which will firstly create the folder then run a for loop from 2 to 20 and will generate table through generateTable
def start():
    folder_path = "09/.Table"
    os.mkdir(folder_path)
    for n in range(2,21):
        table=generateTable(n)
        with open(f"{folder_path}/{n}.txt","w") as f:
            f.write(table)
    else:
        print("Done!")

start()