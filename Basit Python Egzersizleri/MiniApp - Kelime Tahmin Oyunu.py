# Kelime tahmin oyunu.

KeyWord = "Kedi"
Guess = ""
GuessCount = 0
GuessLimit = 10
OutOfGuess = False

while Guess != KeyWord and not(OutOfGuess):
    if GuessCount < GuessLimit:
        Guess = input("enter guess :\t")
        GuessCount += 1
    else:
        OutOfGuess = True

if OutOfGuess:
    print("Unfortunately you loose")
else:
    print("You win")
