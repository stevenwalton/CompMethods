# Guess the number game
import random as r

guesses = 0

name = raw_input('Hello!  What is your name? ')

number = r.randint(1,20)
print(name + "I'm thinking of a number between 1 and 20")

while guesses < 6:       # Gives you 5 guesses
    print('Take a guess.')
    guess = input()
    guess = int(guess)  # Doesn't let users guess non integers

    guesses = guesses + 1

    if guess < number:
        print("Sorry, your guess is too low.")

    if guess > number:
        print("Sorry, your guess is too high.")

    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("Good job," + name + "! You got the number in " + guesses + "guesses!")

if guess != number:
    number = str(number)
    print("Sorry!  The number I was thinking of was" + number)

