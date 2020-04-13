import random
import sys

# again = input("Do you want to play? ")
again = "Yes"

while again == "Yes":

    computer_move = random.randint(1,3)

    computerMoves = {
        1: 'Rock',
        2: 'Paper',
        3: 'Scissors'
        }

    computer_move = computerMoves.get(computer_move)

    your_move = input("Rock, Paper, or Scissors: ")

    yourMove = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissors',
    }

    your_move = yourMove.get(your_move)

    if your_move not in ["Rock", "Paper" ,"Scissors", "r", "p", "s"]:
            sys.exit("Invalid Move: " +your_move)

    print("The computer chose " + computer_move + "!")

    tie = "Tie!"
    you_win = "You Win!"
    you_lose = "You Lose!"

    if computer_move == your_move:
         print(tie)
    elif computer_move == "Rock" and your_move == "Paper":
        print(you_win)
    elif computer_move == "Rock" and your_move == "Scissors":
        print(you_lose)
    elif computer_move == "Paper" and your_move == "Rock":
        print(you_lose)
    elif computer_move == "Paper" and your_move == "Scissors":
        print(you_win)
    elif computer_move == "Scissors" and your_move == "Rock":
        print(you_win)  
    elif computer_move == "Scissors" and your_move == "Paper":
        print(you_lose)
