class Employee:
    name = "Rajveer"
    language = "Python"  # this is a class attribute
    salary = 10000 # this is a class attribute


rajveer = Employee()
rajveer.language = "JavaScript" # this is an instance attribute
print(rajveer.salary, rajveer.language)

# Instance attributes take preference over class attributes during assignment
# & retrieval


