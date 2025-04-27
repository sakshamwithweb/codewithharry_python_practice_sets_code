# Write a class 'Calculator' capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.square = n**2
        self.cube = n**3
        self.square_root = n**0.5


a = Calculator(25)
print(a.square, a.cube, a.square_root)
