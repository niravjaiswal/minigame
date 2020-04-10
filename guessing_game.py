import random

secret_num = random.randint(1,10)
guess = 0
guess_count = 1
guess_limit = 3


while guess != secret_num and guess_count <= guess_limit:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess_count == guess_limit:
      print("You loose") 
    elif guess > secret_num:
      print("Lower, You have " + str(guess_limit - guess_count) + " guesses left")
    elif guess < secret_num:
      print("Higher, You have " + str(guess_limit - guess_count) + " guesses left") 
    else:
      print("You Win!")
    guess_count += 1  

     
