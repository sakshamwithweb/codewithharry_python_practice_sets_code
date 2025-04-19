# Check that a tuple type cannot be changed in python.

t = (1, 2, 3)  # Defining a tuple

print(type(t))  # <class 'tuple'>

t[0] = 5 # TypeError: 'tuple' object does not support item assignment