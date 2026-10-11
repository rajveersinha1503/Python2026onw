# Factorial of a number:

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

number = int(input("Enter a number: "))
a=factorial(number)
print(f"Factorial of {number} is {a}")