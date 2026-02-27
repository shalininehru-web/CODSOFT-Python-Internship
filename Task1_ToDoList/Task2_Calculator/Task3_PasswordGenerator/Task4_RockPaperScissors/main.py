# CodSoft Internship Task 4
# Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input("Enter rock, paper, scissors or exit: ").lower()

    if user == "exit":
        break

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Tie")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You win")

    else:
        print("Computer wins")
