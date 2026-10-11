'''
1 for snake
2 for water
3 for gun
'''
import random
comp= random.choice([1,2,3])

inpDict={"Snake".lower():1, "Water".lower():2, "Gun".lower():3}
revDict={1:"Snake".lower(), 2:"Water".lower(), 3:"Gun".lower()}

input = input("Enter your choice: ").lower()
inputdict=inpDict[input]

print(f"You chose {revDict[inputdict].upper()}\nComputer chose {revDict[comp].upper()}")

if (inputdict == comp):
    print("IT IS A DRAW!")

else:
    if (comp==1 and inputdict==2): #-1
        print("YOU LOSE!")
    elif (comp==1 and inputdict==3): #-2
        print("YOU WIN!")
    elif (comp==2 and inputdict==1): #1
        print("YOU WIN!")
    elif (comp==2 and inputdict==3): #-1
        print("YOU LOSE!")
    elif (comp==3 and inputdict==1): #2
        print("YOU LOSE!")
    elif (comp==3 and inputdict==2): #1
        print("YOU WIN!")
    else:
        print("Something went wrong.")

    # if (comp-inputdict==2 or comp-inputdict==-1):
    #     print("YOU LOSE.")
    # else:
    #     print("YOU WIN.")
