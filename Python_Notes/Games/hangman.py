# Hangman game
import random as r
import csv
import os

# First thing we need to do is create the drawings that will be used.  Time to employ your ascii art skills.
# You can get more creative and import pictures, but I will leave that for the student to solve.  We will
# probably go over pictures and graphs later.  But for now let's do this oldschool.
HANGMANPICS = ['''
 +---+
 | |
   |
   |
   |
   |
=======''','''
 +---+
 | |
 O |
   |
   |
   |
=======''','''
 +---+
 | |
 O |
 | |
   |
   |
=======''','''
 +---+
 | |
 O |
/| |
   |
   |
=======''','''
 +---+
 | |
 O |
/|\|
   |
   |
=======''','''
 +---+
 | |
 O |
/|\|
/  |
   |
=======''','''
 +---+
 | |
 O |
/|\|
/ \|
   |
=======''']

# We need to create a dictionary of words.  Instead of having it here, we are going to make the program a little more advanced and user friendly by using a user defined dictionary.  There will be one word per line in the text
# file that can be modified at will.


### use if you want a set list of words
#dictionary = 'ant baboon badger'.split()          

# use if you want to have a file of words that can be read (a dictionary per say)
dictionary = []
with open('wordlist.txt', 'rb') as csvfile:
    # This list was made in a way that there is a word on each line.  No commas or anything, just \n between words
    reader = csv.reader(csvfile, delimiter=' ')
    dictionary = list(reader)

# We want our program to pick a random word from our dictionary
def getRandomWord(WordList):
    # We're going to pick a random element of our list
    wordIndex = r.randint(0, len(WordList)-1)
    # We need to get rid of the commas from the list.  Otherwise we will have non-character inputs for our game
    return ', '.join(WordList[wordIndex])

# We want to display the board, this function will do this
def displayBoard(HANGMANPICS, missedLetters, correctLetters, word):
    # We're going to print which hangman pic we need.  Which is chosen by the number of missed letters
    print HANGMANPICS[len(missedLetters)]
    
    # We also want to display the letters that we have missed, so that we don't guess them again
    print "Missed letters: " + missedLetters

    # We'll print the blanks so that we know how many letters the word is.
    blanks = '_' * len(word)
    # We are also filling in those blanks with the letters that we have guessed correctly.
    for i in range(len(word)):
        if word[i] in correctLetters:
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    print blanks

# Let's make a function to gather the user input for guesses.  It's easier to define this as a function
def getGuess(alreadyGuessed):
    while True:
        guess = raw_input("Guess a letter: ")
        guess = guess.lower()                       # This is so we can only work with one case.  That'll show those CAPITALISTS
        if len(guess) != 1:
            print "Please enter a single letter..."
        elif guess in alreadyGuessed:
            print "You already guessed that letter!!"
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print "Please print an English letter..."
        else:
            return guess
# Notice what I said before about not assuming your user is intelligent.  They might be intelligent but just like breaking programs (which is the best way to learn how it works, might I add).



# Let's clear the screen every time we start a new game or finish.  You can also make this clear every loop
def clearScreen():
    try:                    # Try literally tries something, and if it doesn't work just continues
        os.system('cls')    # this works for windows
    finally:                # Executes no matter what.  This is an assumption that if they aren't on winblows
                            # then they are on a *nix machine.  Can this cause problems?  (Answer is probably).
                            # Student is left to research different errors and exceptions to solve this.
        os.system('clear')  # this is for *nix machines (linux, osx, unix)


#Obviously our game is so great that we will want to play it again.  Right?  Well let's let the user decide
def playAgain():
    again = raw_input("Would you like to play again?(y/n): ").lower()
    if "y" in again: # Note that this will run if they type any word with a y in it.  Left as an exercise for the 
                     # student.  How can get words like "type" not to return a new game?
        return True

# Now that we are done with our definitions we will get to the actual game.

# Question for student, why do we not add this as the first line of the while loop? Why here?
print "H A N G M A N"
missedLetters = ''                                  # We always want to initialize variables
correctLetters = ''
word = getRandomWord(dictionary)
gameIsDone = False

while True: 
    # We're going to clear the screen and print the title every time the loop executes.  This keeps things clean
    # It's a lot more professional looking than if we don't
    clearScreen()
    print "H A N G M A N"

    # Now is when we will start using the definitions that we created earlier.  Note that input names don't
    # have to match the name we gave them in the definition, only the place.
    displayBoard(HANGMANPICS, missedLetters, correctLetters, word)
    

    # The rest shoudl be easily readable and understandable by the student at this point.
    guess = getGuess(missedLetters + correctLetters)

    if guess in word:
        correctLetters = correctLetters + guess

        foundAllLetters = True                      # We even initialize this
        for i in range(len(word)):
            if word[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
             print "Good job!  The word was " + word + " You WIN!!!!"
             gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS, missedLetters,correctLetters,word)
            print "OH NO!!!! You ran out of guesses and let the man die.  He could have been innocent! The correct word was " + word
            gameIsDone = True
    if gameIsDone:
        if playAgain() is True:
            clearScreen()
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            word = getRandomWord(dictionary)
        else:
            clearScreen()
            break
