class Employee:
    name = "Rajveer"
    language = "Python"  # this is a class attribute
    salary = 10000 # this is a class attribute


rajveer = Employee()
rajveer.name = "Rajveer" # this is an instance attribute
print(rajveer.name, rajveer.salary, rajveer.language)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance/object attribute and salary and language are class attributes
# as they directly belong to the class

