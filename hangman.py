def hangman():
    word = "dulce"
    word_list = ["d", "u", "l", "c", "e"]
    word_list2 = ["_", "_", "_", "_", "_"]
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
            print(word_list2)


            for index, char in enumerate(word_list):
                # if the char is the guess
                # then update the index in the word_list2 to be that char
                if char == guess:
                    word_list2[index] = guess
                    print(word_list2)





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


#figure out all of the places that the char exists in the word
#find all of the positiions of where it's in the word
#update the correct position in the list to be that guess









#
