# Write a program to detect double space in a string.

string = input("Enter a sentance: ")  # Get sentance

# Alert about the output
print("If I return -1 means doesn't contain double space or else it contains")

# Checking whether it contains double space or not, if does so it will return positive index or else -1
value = string.find("  ")

print(f"\nOutput: {value}\n")  # using f string
