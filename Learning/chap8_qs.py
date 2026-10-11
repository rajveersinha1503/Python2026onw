# PROBLEM 1:
# def greatest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
#
# print("Enter three numbers:")
# a=int(input())
# b=int(input())
# c=int(input())
# print(f"Greatest number out of {a},{b} and {c} is {greatest(a,b,c)}")

# PROBLEM 2:
# def ctf(c):
#     return (c*1.8)+32
#
# c=float(input("Enter temperature in Celsius: "))
# print(f"Temperature in Fahrenheit: {round(ctf(c),2)}°F")

# PROBLEM 3:
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# PROBLEM 4:
# def sum(a):
#     if(a==1):
#         return 1
#     else:
#         return a+sum(a-1)
#
# a=int(input("Enter number upto which sum is required: "))
# print(f"Sum of natural numbers upto {a} is {sum(a)}")

# PROBLEM 5:
# def pattern(n):
#     if (n==0):
#         return
#     else:
#         print("*"*n)
#         pattern(n-1)
#
# n=int(input("Enter number of lines: "))
# pattern(n)

#           OR

# def pattern(n):
#     for i in range(1,n+1):
#         print("*"*(n+1-i),end="")
#         print()
#
# n=int(input("Enter number of lines: "))
# pattern(n)

#           OR

# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             print("*",end=" ")
#         print()
#
# n=int(input("Enter number of lines: "))
# pattern(n)

# PROBLEM 6:
# def inch_to_cm(inch):
#     return float (inch*2.54)
#
# inch=float(input("Enter measurement in inches: "))
# print(f"Measurement in inches: {inch_to_cm(inch)} cm")

# PROBLEM 7:
# def remove(l,word):
# 	n=[]
# 	for i in l:
# 		if (i!=word):
# 			n.append(i.strip(word))
# 	return n
#
# l=["Harry","Shubham","Rohan","an"]
# word=input("Enter word to be removed and stripped: ")
# print(remove(l,word))

# PROBLEM 8:
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

n=int(input("Enter the number for which table is to be printed: "))
table(n)
