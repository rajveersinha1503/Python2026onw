# PROBLEM 1:
# f= open("poem.txt")
# contents = f.read()
#
# if ("twinkle" in contents):
#     print("The word twinkle is present")
# else:
#     print("The word twinkle is not present")
#
# f.close()

# PROBLEM 2:
# import random
# def game():
#     print("You are playing the game..")
#     score = random.randint(1,100)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if (hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#
#     print(f"Your score: {score}")
#     if (score > hiscore or hiscore == ""):
#         with(open("hiscore.txt","w")) as f:
#             f.write(str(score))
#
#     return score
#
# game()

# PROBLEM 3:
# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)
#
# for i in range(2,21):
#     generateTable(i)

# PROBLEM 4:
# with open ("filecheck.txt", "r") as f:
#     content = f.read()
#
# contentnew = content.replace("Donkey","#####")
#
# with open("filecheck.txt", "w") as f:
#     f.write(contentnew)

# PROBLEM 5:
# words = ["Donkey","gande","bad"]
# with open ("donkey.txt", "r") as f:
#     content = f.read()
#
# for word in words:
#     content = content.replace(word,"#"*len(word))
#
# with open ("donkey.txt", "w") as f:
#     f.write(content)

# PROBLEM 8:
# with open("this.txt") as f:
#     content = f.read()
#
# with open("thiscopy.txt","w") as f:
#     contentc = f.write(content)

# PROBLEM 9:
# with open("this.txt") as f:
# 	content = f.read()
#
# with open("thiscopy.txt") as f:
#     contentc = f.read()
#
# if (content == contentc):
#     print("Both files are identical")
# else:
#     print("Both files are not identical")

# PROBLEM 10:
# with open("file.txt","w") as f:
#     f.write("")

# PROBLEM 11:
import os
with open("old.txt") as f:
    contentc = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(contentc)

os.remove("old.txt")



