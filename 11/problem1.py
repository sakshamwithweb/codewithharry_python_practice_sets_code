# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}")


two_d = Vector2D(1,2)
two_d.show()

three_d = Vector3D(1, 2, 3)
three_d.show( )