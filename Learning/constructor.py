class Employee():
    language = "Python"  # this is a class attribute
    salary = 10000 # this is a class attribute

    def __init__(self,name,salary,language):#Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    # def getInfo(self):
    #     print(f"Language: {self.language}, Salary: "f"{self.salary}")

    @staticmethod
    def greet():
        print(f"Good morning!")

rajveer = Employee("Rajveer",120000,"JavaScript")
print(rajveer.name, rajveer.salary,rajveer.language)
rajveer.greet()

rohan = Employee("Rohan",100000,"Python")
print(rohan.name, rohan.salary,rohan.language)
rohan.greet()