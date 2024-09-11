import random
user_wins=0
computer_wins=0
options= ["rock","paper","sissors"]

while True:
    user_input=input("Type Rock/Papers/Sissors or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        print("Not Valid Input")
        continue

    random_no=random.randint(0,2)
    computer_pick=options[random_no]
    print("computer guess is ", computer_pick+".")

    if user_input=="rock" and computer_pick=="sissors":
        print("You won!")
        user_wins+=1
    elif user_input=="sissors" and computer_pick=="paper":
        print("You won!")
        user_wins+=1    
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1  
    else:
        print("You Loss!")
        computer_wins+=1
print("Score: ", str(user_wins) + "-", str(computer_wins))
if user_wins>computer_wins:
    print("You win")
elif user_wins<computer_wins:
    print("You loss")
else:
    print("Draw")
      


