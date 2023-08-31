import random


options = ["rock", "paper", "scissors"]
userScore = 0
computerScore = 0




def game(user, computer):
    global userScore
    global computerScore

    if user == computer:
        print("No one winner... It's tie")
    
    elif user == "rock":
        if computer == "scissors":
            userScore += 1
            print(f"user has {userScore} points")
        else:
            computerScore += 1
            print(f"computer has {computerScore} points")

    elif user == "paper":
        if computer == "rock":
            userScore += 1
            print(f"user has {userScore} points")
        else:
            computerScore += 1
            print(f"computer has {computerScore} points")

    elif user == "scissors":
        if computer == "paper":
            userScore += 1
            print(f"user has {userScore} points")
        else:
            computerScore += 1
            print(f"computer has {computerScore} points")



while True:
    if userScore == 5:
        print("-"*30)
        print(f"User win with {userScore} score!")
        print("-"*30)
        exit()
    elif computerScore == 5:
        print("-"*30)
        print(f"Computer win with {userScore} score!")
        print("-"*30)
        exit()

    userChoice = input("Enter a choice (rock, paper, scissors): ").lower()
    computerChoice = random.choice(options)

    if userChoice not in options:
        print("Invalid choice... try again")
    else:
        game(userChoice, computerChoice)
    
