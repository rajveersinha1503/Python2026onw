# PROBLEM 1
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# PROBLEM 2
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello {name}!")
#     else:
#         print(f"Fuk off {name}!")

# PROBLEM 3
# n=int(input("Enter a number: "))
# i=1
# while (i<11):
#     print(f"{n} x {i} = {n*i}")
#     i=i+1

# PROBLEM 4
# n=int(input("Enter a number: "))
# c=0
# for i in range(1,n+1):
#     if(n%i==0):
#         c+=1
# if(c==2):
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#               OR

# n=int(input("Enter a number: "))
# for i in range(2,n):
#     if (n%i==0):
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is a prime number")

# PROBLEM 5
# n=int(input("Enter a number: "))
# s=0
# for i in range(1,n+1):
#     s=s+i
# print(f"Sum of first {n} natural numbers is {s}")

#                 OR

# n=int(input("Enter a number: "))
# i=1
# s=0
# while (i<=n):
#     s=s+i
#     i=i+1
# print(f"Sum of first {n} natural numbers is {s}")

# PROBLEM 6
# n=int(input("Enter a number: "))
# p=1
# for i in range(1,n+1):
#     p=p*i
# print(f"Factorial of {n} is {p}")

# PROBLEM 7
# n=int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(i),end="")
#     print("*"*(i-1),end="")
#     print(" "*(n-i),end="")
#     print("\n")

#           OR

# n=int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print(" "*(n-i),end="")
#     print("\n")

# PROBLEM 8
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):    ### NESTED LOOP METHOD
#         print("*",end="")
#     print("\n")

#             OR

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):                     ### WITHOUT NESTED LOOP
#     print("*"*(i),end="")
#     print("\n")

# PROBLEM 9
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("\n")

# PROBLEM 10
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} x {11-i} = {n*(11-i)}")

#              OR

n = int(input("Enter a number: "))
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")
