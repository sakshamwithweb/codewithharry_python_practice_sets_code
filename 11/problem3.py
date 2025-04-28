# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return (self.salary+(self.salary*self.increment)/100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = 100*((salary-self.salary)/self.salary)

em1 = Employee("Saksham", 120,0)
em1.salaryAfterIncrement = 198
print(em1.increment)