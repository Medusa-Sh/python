import random
playing=True
number=str(random.randint(0,9))
print("I will generate a random number between 0 and 9. Can you guess it?")
print("The game ends when you get 1 hero")
while playing:
    guess=input("Now please enter your guess: ")
    if guess==number:
        print("You win!")
        print("The number was",number)
        break

    else:
        print("Wrong guess. Try again.\n")