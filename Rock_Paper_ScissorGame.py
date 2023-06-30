import random

ComputerScore = 0
UserScore = 0
computer_choices = ["Rock", "Paper", "Scissor"]
i = 1
rounds = int(input("How many rounds?: "))

while i <= rounds:
    print(f"\nRound {i}\nPick: [Rock, Paper, Scissor]")
    userInput = input(">>> ").capitalize()
    computerInput = random.choice(computer_choices)

    #Computer Scoring Logic Flow-----------------------------------------
    if computerInput == "Rock" and userInput == "Scissor":
        print(f"\n[Round {i}: Computer Wins {computerInput} beats {userInput}]")
        ComputerScore += 1

    elif computerInput == "Paper" and userInput == "Rock":
        print(f"\n[Round {i}: Computer Wins {computerInput} beats {userInput}]")
        ComputerScore += 1

    elif computerInput == "Scissor" and userInput == "Paper":
        print(f"\n[Round {i}: Computer Wins {computerInput} beats {userInput}]")
        ComputerScore += 1

    #User Scoring Logic Flow---------------------------------------------
    elif userInput == "Rock" and computerInput == "Scissor":
        print(f"\n[Round {i}: User Wins {userInput} beats {computerInput}]")
        UserScore += 1

    elif userInput == "Paper" and computerInput == "Rock":
        print(f"\n[Round {i}: User Wins {userInput} beats {computerInput}]")
        UserScore += 1

    elif userInput == "Scissor" and computerInput == "Paper":
        print(f"\n[Round {i}: User Wins {userInput} beats {computerInput}]")
        UserScore += 1

    elif userInput == computerInput:
        print(f"\n[Round {i}: Tie, {userInput} tie {computerInput}]")

    i +=1

#Tells who wins
if UserScore > ComputerScore:
    print(f"\nUser Wins, Score: User[{UserScore}] Computer[{ComputerScore}]")
elif ComputerScore > UserScore:
    print(f"\nComputer Wins, Score: User[{UserScore}] Computer[{ComputerScore}]")
else:
    print("\nIt's a tie!")