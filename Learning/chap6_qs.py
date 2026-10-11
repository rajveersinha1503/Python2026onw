# PROBLEM 1
# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))
#
# if(a1>a2 and a1>a3 and a1>a4):
#     print(a1," is the greatest number")
#
# elif(a2>a1 and a2>a3 and a2>a4):
#     print(a2," is the greatest number")
#
# elif(a3>a1 and a3>a2 and a3>a4):
#     print(a3," is the greatest number")
#
# elif(a4>a1 and a4>a2 and a4>a3):
#     print(a4," is the greatest number")

# PROBLEM 2
# m1=int(input("Enter marks in Science: "))
# m2=int(input("Enter marks in Mathematics: "))
# m3=int(input("Enter marks in English: "))
#
# total_percentage= ((m1+m2+m3)/300)*100
# if(total_percentage>=40 and m1>=33 and m2>=33 and m3>=33):
#     print("Student has passed: ",total_percentage)
# else:
#     print("Student has failed: ",total_percentage)

# PROBLEM 3
# p1="Make a lot of money"
# p2="Buy now"
# p3="Subscribe this"
# p4="Click this"
#
# message= input("Enter your comment: ")
#
# if((p1.lower() in message.lower()) or (p2.lower() in message.lower()) or
#         (p3.lower() in message.lower()) or (p4.lower() in message.lower())):
#     print("Spam message")
# else:
#     print("Not a spam message")
#
# PROBLEM 4
# username= input("Enter username: ")
# if (len(username)<10):
#     print("Username has less than 10 characters")
# else:
#     print("Username has more than 10 characters")

# PROBLEM 5
# print("Enter 5 names in a list:\n")
# name_list=[input() for x in range(5)]
# name=input("Enter name to be searched: ");
# if (name in name_list):
#     print("Name is in the list")
# else:
#     print("Name not found")

#           OR

# l = ["Harry", "Rohan", "Shubham", "Divya"]
#
# name = input("Enter your name: ")
#
# if(name in l):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

# PROBLEM 6
# A=int(input("Enter your marks of subject A: "))
# B=int(input("Enter your marks of subject B: "))
# C=int(input("Enter your marks of subject C: "))
# D=int(input("Enter your marks of subject D: "))
# E=int(input("Enter your marks of subject E: "))
#
# percentage=((A+B+C+D+E)/500)*100
# print(percentage)
#
# if (percentage>=90 and percentage<=100):
#     print("Your grade is Ex")
# elif (percentage>=80 and percentage<90):
#     print("Your grade is A")
# elif (percentage>=70 and percentage<80):
#     print("Your grade is B")
# elif (percentage>=60 and percentage<70):
#     print("Your grade is C")
# elif (percentage>=50 and percentage<60):
#     print("Your grade is D")
# elif (percentage<50):
#     print("Your grade is F")

# PROBLEM 7
# post=input("Enter a post: ")
# if("Harry".lower() in post.lower()):
#     print("The post is talking about Harry")
# else:
#     print("The post is not talking about Harry")

