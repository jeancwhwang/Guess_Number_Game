# This is a guess the number game
import random

print("Hello! Let's play a game. Guess a number between 1 and 10.")
computerNumber = random.randint(1,10)

# Ask the player to guess 5 times
for guessTaken in range (1,6) :
    playerGuess = int(input("Please enter your number here:"))

    if playerGuess > computerNumber and playerGuess in range (1,10):
        print("You typed" +" "+ str(playerGuess) +"." + "It is higher than the answer.")
    elif playerGuess < computerNumber and playerGuess in range (1,10):
        print("You typed" + " " + str(playerGuess) + "." + "It is lower than the answer.")
    else:
        break

if playerGuess == computerNumber:
    print ("Bingo!"+" "+ "You guessed my number in" + " " + str(guessTaken) + " " + "guess!" )

else:
    print("Nope! The number I was thinking of was" + " " + str(computerNumber))
