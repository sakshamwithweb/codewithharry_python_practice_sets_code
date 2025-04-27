# Write a Class 'Train' which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random

class Passenger:
    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def book(self):
        print(f"Ticket has been booked successfully for Train no:{self.trainNo} from {self.fro} to {self.to}")
    
    def status(self):
        print(f"Train no: {self.trainNo} is leaving {self.fro} for {self.to}")

    def fare(self):
        print(f"Ticket fair in train no: {self.trainNo} from {self.fro} to {self.to}, is ₹{random.randint(200,2000)}")


passenger1 = Passenger(123456,"Raipur","New Delhi")
passenger1.fare()