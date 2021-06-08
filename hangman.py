def hangman():
    word = "dulce"
    guesses = ""
    turns = 10
    failed = 0

    while turns > 0:
        guess = input("Guess a letter! ")
        if guess in word:
            failed = 0
            turns -= 1
            guesses += guess
            print(f"Good guess! You have {turns} guesses left. {guesses}")
        elif guess not in word:
            failed += 1
            turns -= 1
            guesses += "-"
            print(f"Wrong! Guess again! You have {turns} guesses left. {guesses}")

        if turns == 0:
            print("You are out of guesses!")

        if turns != 0 and failed == 0:
            print("You win!")
hangman()












#
