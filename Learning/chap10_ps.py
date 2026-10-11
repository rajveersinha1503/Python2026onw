# PROBLEM 1:
# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,salary,pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode
#
#     def greet(self):
#         print(f"Good morning {self.name}!")
#
#
#
# p = Programmer("Rajveer",100000,"700034")
# p.greet()
# print(p.name,p.salary,p.pincode)
#
# r = Programmer("Rohan",120000,"800091")
# r.greet()
# print(r.name,r.salary,r.pincode)

# PROBLEM 2:
# import math
# class Calculator:
#     def __init__(self,num):
#         self.num = num
#
#     @staticmethod
#     def greet():
#         print("Hello there!")
#
#     def square(self,num):
#         return num*num
#
#     def cube(self,num):
#         return num*num*num
#
#     def sqrt(self,num):
#         return math.sqrt(num)
#
#
# n = int(input("Enter a number: "))
#
# cal = Calculator(n)
# cal.greet()
# print(f"Square of {n}: {cal.square(n)}")
# print(f"Cube of {n}: {cal.cube(n)}")
# print(f"Square root of {n}: {cal.sqrt(n)}")

# PROBLEM 3:
# class object:
#     a = 20
#
# o = object()
# print(o.a) # Prints the class attribute because instance attribute is not present
# o.a = 0 # Instance attribute is set
# print(o.a) # Prints the instance attribute as it is preferred over clss attribute
# print(object.a) # Prints the class attrbute

# PROBLEM 4:
from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train number {self.trainNo} "
              f"from {fro} to {to}")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running successfully")

    def getFare(self,fro,to):
        print(f"Ticket fare in train number {self.trainNo} "
              f"from {fro} to {to} is {randint(222,5555)}")


t = Train(12399)

t.book("Howrah","Jamalpur")
t.getStatus()
t.getFare("Howrah","Jamalpur")