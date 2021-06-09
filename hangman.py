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
            print(f"Good guess! You have {turns} guesses left. Current guesses: {guesses}")
            # print(word_list2)


            for index, char in enumerate(word_list):
                # if the char is the guess
                # then update the index in the word_list2 to be that char
                if char == guess:
                    word_list2[index] = guess
                    print(word_list2)





        elif guess not in word:
            failed += 1
            turns -= 1
            guesses += guess
            print(f"Wrong! Guess again! You have {turns} guesses left. Current guesses: {guesses}")
            print(word_list2)

        if word_list2 == word_list:
            print("You won the game! \U0001F929")

        if turns < 1:
            print("You are out of guesses! Game over! \U0001F622")



        # if turns != 0 and failed == 0:
        #     print("You win!")
hangman()


#figure out all of the places that the char exists in the word
#find all of the positiions of where it's in the word
#update the correct position in the list to be that guess


#IDEAS WHEN REFACTORING:
# def play():
    # hangman = 'boolean'
#   blank = ['_'] * len(hangman)

# elif guessed_word in blank:
    # print('Sorry you already guessed that letter')


# word = input('Player1: Please enter a lowercase word: ') *use method to convert to lowercase just incase user does not follow directions!




#
