# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

try:
    num: int = int(input("Enter number: "))
    table = [x*num for x in range(1,11)]
    with open("12/table.txt","a") as f:
        f.write(str(table)+"\n")

        # table = [str(x) for x in table]
        # f.write("\n".join(table))
except ValueError:
    print("I said numberr")

except Exception as e:
    print(e)