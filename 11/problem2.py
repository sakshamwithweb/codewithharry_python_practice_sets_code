# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def greet(self):
        print(f"Hey I am {self.name}")


class Pets(Animals):
    def __init__(self, name, ownerName, vegeterian):
        self.vegeterian = vegeterian
        self.ownerName = ownerName
        super().__init__(name)

    def ownerNameIntro(self):
        print(f"My owner is {self.ownerName}")

    def isVegeterian(self):
        print(f"Am I vegeterian: {self.vegeterian}")


class Dog(Pets):
    def __init__(self, name, ownerName, vegeterian):
        super().__init__(name, ownerName, vegeterian)
    
    def bark(self):
        print("Bhaou Bhaou!")


tommy = Dog("Tommy","Saksham",True)

tommy.greet()
tommy.eat()
tommy.bark()
tommy.ownerNameIntro()
tommy.isVegeterian()    
tommy.sleep()