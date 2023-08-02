import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    randnum = random.randint(0,2)
    #picking up a random number for computer's turn

    comp_pick = options[randnum]
    print("computer pick",comp_pick,".")

    if user_input == "rock" and comp_pick== "scissors":
        print("You won!")
        user_wins+=1
    elif user_input == "paper" and comp_pick== "rock":
        print("You won!")
        user_wins+=1
    elif user_input == "scissors" and comp_pick== "spaper":
        print("You won!")
        user_wins+=1
    else:
        print("You Lost")
        computer_wins+=1
#displaying results
print("You won",user_wins,"times.")
print("The computer won",computer_wins,"times.")


print("Bye!")
    

