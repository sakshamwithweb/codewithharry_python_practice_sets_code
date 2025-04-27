# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.square = n**2
        self.cube = n**3
        self.square_root = n**0.5
    
    @staticmethod
    def greet():
        print("Hello there!")


a = Calculator(25)
print(a.square, a.cube, a.square_root)
