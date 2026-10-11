a=int(input("Enter your age: "))
# If statement-1:
if(a%2==0):
    print("You are an even age")
# End of if statement-1

# If statement-2:
if(a>=18):
    print("You are above the age of consent") # The gap is called indentation
    print("Good for you")

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("Invalid age")

else:
    print("You are below the age of consent")
# End of if statement-2
print("End of program")
