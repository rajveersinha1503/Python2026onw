class Employee():
    language = "Python"  # this is a class attribute
    salary = 10000 # this is a class attribute

    def getInfo(self):
        print(f"Language: {self.language}, Salary: "f"{self.salary}")

    @staticmethod
    def greet():
        print(f"Good morning!")

rajveer = Employee()
rajveer.name = "Rajveer"
rajveer.language = "JavaScript" # this is an instance attribute

rajveer.greet()
rajveer.getInfo()
# Employee.getInfo(rajveer)

rohan = Employee()
rohan.name = "Rohan"
rohan.greet()
rohan.getInfo()
