import random
options = ["rock", "paper", "scissors"]
ur_choice = input("choose rock, paper, or scissors (btw this is the world cup): ")
ai_choice = random.choice(options)
print("you chose: ", ur_choice)
print("the ai chose: ", ai_choice)
if ur_choice == ai_choice:
    print("TIE retry this round!")
elif ur_choice == "rock" and ai_choice == "scissors":
    print("ugh fine you win this time🙄🙄")
elif ur_choice == "paper" and ai_choice == "rock":
    print("ugh fine you win this time🙄🙄")
elif ur_choice == "scissors" and ai_choice == "paper":
    print("ugh fine you win this time🙄🙄")
else:
    print(" BLUD U JUST SOLD IN ROCK PAPER SCISSORS IN FRONT THE ENTIRE WORLD DURING THE WORLD CUP U LITTLE FAILURE")