a=int(input("Enter your age: "))

# If-elif-else ladder

if(a>=18):
    print("You are above the age of consent") # The gap is called indentation
    print("Good for you")

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("Invalid age")

else:
    print("You are below the age of consent")
print("End of program")
