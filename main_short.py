import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}

you = youDict[youstr]

#By now we have 2 numbers(variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw")
else:
    '''
    if(computer == -1 and you == 1):-2
        print("You win")
    elif(computer == -1 and you == 0): -1 
        print("you lose")
    elif(computer == 1 and you == -1): 2
        print("You lose")
    elif(computer == 1 and you == 0): 1
        print("You win")
    elif(computer == 0 and you == -1): 1
        print("You win")
    elif(computer == 0 and you == 1): -1
        print("You lose")
    
      The below logic is return on the basis of the value of computer-you
    
      '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You win!")