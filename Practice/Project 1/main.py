import random
'''
1 for stone
-1 for paper
0 for scissor
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1,"p": -1,"c": 0}
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

you = youDict[youstr]

# by now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You win!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 0):
        print("You win!")
    else:
        ("Something went wrong")