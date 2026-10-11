# Average of three numbers

# Function definition
# def avg():
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     c=int(input("Enter another number: "))
#
#     avg=(a+b+c)/3
#     print("The average is ",avg)
#
# avg() # Function call
# avg()
# avg()
# avg()

def avg():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=int(input("Enter another number: "))

    avg=(a+b+c)/3
    return avg

a=avg()
print("Average = ",a)
