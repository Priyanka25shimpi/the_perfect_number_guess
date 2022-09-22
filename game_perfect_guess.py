import random
randomNumber = random.randint(1,100)
userGuess = None
guesses = 0

while (userGuess != randomNumber):
    userGuess = int(input("Enter the Guess..."))
    guesses += 1
    if(userGuess == randomNumber):
        print("Your Guess is right !!")
    else:
        if(userGuess>randomNumber):
            print("You Guessed it wrong. please get smaller number.")
        else:
            print("You Guessed it wrong. please get greater number.")
print(f"You guessed the number with {guesses} guesses.")
with open("highscore_perfect_guess.txt") as f:
    highscore = int(f.read())
    if(guesses<highscore):
        print("you cracked the highscore !!")
with open("highscore_perfect_guess.txt", "w") as f:
    f.write(str(guesses))