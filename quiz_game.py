#this game asks users a bunch of questions and if they get them, 1 mark is added to their score
print("Welcome to Somies Quiz!")
game= input("Do you want to play Somie's Quiz Game- ")
if game.lower() == "yes":
    print("Lets begin the game!")
    answer1 = "2"
    question1 = input("How many colours are on the Nigerian flag- ")
    if question1 == answer1:
        print("Your answer is correct!")
    else:
        print(f"Your answer is wrong. The right answer is {answer1}")

    answer1 = "Britian"
    answer2 = "Great Britian"
    question1 = input("Which country colonized Nigeria- ")
    if question1.lower() == answer1 or question1.lower() == answer2:
            print("Your answer is correct!")
    else:
            print(f"Your answer is wrong. The right answer is {answer1}")

    answer1 = "strength"
    question1 = input("What does the horse on the Nigerian coat of arms represent?")
    if question1.lower() == answer1:
        print("Your answer is correct!")
    else:
        print(f"Your answer is wrong. The right answer is {answer1}")

    #answer1 = "No"
    # question1 = input("Is it right to murder someone?")
    #     if question1 == answer1:
    #         print("Your answer is correct!")
    #     else:
    #         print(f"Your answer is wrong. The right answer is {answer1}")
    #
    # answer1 = "36"
    # answer2 = "36 states"
    # question1 = input("How many states are in Nigeria?")
    # if question1 == answer1 or question1 == answer2:
    #     print("Your answer is correct!")
    # else:
    #     print(f"Your answer is wrong. The right answer is {answer1}")


else:
    print("The game ends here!")