import random
user_score = 0
computer_score = 0
computer_random = random.randint(0,2)
# NB: Rock-0 , Paper-1, Scissors-2
# We made a list containing the rock, paper and scissors and then we want to acess it
# computer_options = ["R","P","S"]
# computer_pick = computer_options[random.randint(0,2)]
# print(f"The computer picked,{computer_pick}")
print("Enter Q - Quit game","R -Rock, P - Paper, S - Scissors")

while True:
    answer = input("Enter Rock, Paper or Scissors ").upper()
    if answer == "Q":
        print("You would be logged out of the game now!")
        quit()
    if answer not in ["R","P","S"]:
        print("This is not a valid input")
    else:
        computer_options = ["R", "P", "S"]
        computer_pick = computer_options[random.randint(0, 2)]
        print(f"The computer picked,{computer_pick}")

        if computer_pick == answer:
            print("You guessed correctly!")
            user_score += 1
            print(f"You won {user_score} over the computer!")
        else:
            print("You guessed wrongly!")
            print("Start Again")
            continue
        continue