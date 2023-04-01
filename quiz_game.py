#This game asks users a bunch of questions and if they get them, 1 mark is added to their score
print("Welcome to Somies Quiz!")
game = input("Do you want to play Somie's Quiz Game- ")
if game.lower() == "yes":
    print("Lets begin the game!")
    score = 0
else:
    print("The game ends here!")
    quit()

question1 = input("How many colours are on the Nigerian flag- ")
answer = "2"
if question1 == answer:
    print("Your answer is correct!")
    score += 1
else:
    print(f"Your answer is wrong. The right answer is {answer}")

question2= input("Which country colonized Nigeria- ")
answer = "britian"
if question2.lower() == answer:
    print("Your answer is correct!")
    score +=1
else:
    print(f"Your answer is wrong. The right answer is {answer}")

question3= input("What does the horse on the Nigerian coat of arms represent?")
answer = "strength"
if question3.lower() == answer:
    print("Your answer is correct!")
    score+=1
else:
    print(f"Your answer is wrong. The right answer is {answer}")

question4 = input("Is it right to murder someone?")
answer= "no"
if question4.lower() == answer:
    print("Your answer is correct!")
    score+=1
else:
    print(f"Your answer is wrong. The right answer is {answer}")

print("This brings us to the end of the quiz!")
if str(score) >= "3":
    print(f"You did Great, Your score is  "+ str(score)+ "  over 4 ")
else:
    print(f"You can do better! Your score is  "+ str(score)+ "  over 4 ")

