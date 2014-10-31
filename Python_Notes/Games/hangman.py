# Hangman game
import random as r
import csv

# First thing we need to do is create the drawings that will be used.  Time to employ your ascii art skills.
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
dictionary = []                                     # Create an array dictionary. We don't know it's size yet, but that will be perfectly okay
with open('wordlist.txt') as inputfile:  # Now we open a textfile called "wordlist.txt" that is assumed to be in our same directory.  We also note that the character used to seperate words is a new line
    #dictionary = csv.reader(inputfile, delimiter=' ')
    dictionary = list(csv.reader(inputfile, delimiter=' '))
    dictionary = " ".join(map(str,dictionary))
          
# We want our program to pick a random word from this list
def getRandomWord(WordList):
    wordIndex = r.randint(0, len(WordList)-1)
    return WordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, word):
    print HANGMANPICS[len(missedLetters)]
    
    print "Missed letters: " + missedLetters

    blanks = '_' * len(word)

    for i in range(len(word)):
        if word[i] in correctLetters:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]

    for letter in blanks:
        print letter

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

def playAgain():
    again = raw_input("Would you like to play again?(y/n): ").lower
    if 'y' in again: return True

# Now that we are done with our definitions we will get to the actual game.
print "H A N G M A N"
missedLetters = ''                                  # We always want to initialize variables
correctLetters = ''
word = getRandomWord(dictionary)
gameIsDone = False

while True: 
    displayBoard(HANGMANPICS, missedLetters, correctLetters, word)
    
    guess = getGuess(missedLetters + correctLetters)

    if guess in word:
        correctLetters = correctLetters + guess

        foundAllLetters = True                      # We even initalize this
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
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            word = getRandomWord(dictionary)
        else:
            break


