import random

def getGuess():
    print "What is your guess?"
    guess = int(raw_input())
    return guess

def printHigherLower(playerGuess, chosenNumber):
    if playerGuess > chosenNumber:
        print "Lower"
    else:
        print "Higher"

number = random.randint(1, 100)
guess = getGuess()

while guess != number:
    printHigherLower(guess, number)
    guess = getGuess()

print "You win!"
