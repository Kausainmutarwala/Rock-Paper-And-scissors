import random

print("Welcome to the Rock Paper Scissors Game!")

choices = ["rock","paper","scissors"]

user = input(" enter your choice (rock, paper, or scissors): ").lower()

computer = random.choice(choices)

print("computer:", computer)

if user == computer:
    print("it's a tie!")
elif user == "rock" and computer =="scissors":
    print("you win ")
elif user =="paper" and computer =="rock":
    print("you win ")
elif user == "scissors"  and computer == "paper":
    print("you win ")

    
elif computer == "rock" and user == "scissors" :
    print("computer wins")
elif computer == "paper" and user =="rock":
    print("computer wins")
elif computer == "scissiors" and user == "paper":
    print("computer wins")

    
else:
    print("invalid input , firse try karo")
