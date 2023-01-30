This is a Python script for the Hangman game, played in the terminal. The following files are present: 
    hangman_art.py >> used for the art in the game
    hangman_words.py >> used for storing the list of words from where a random one will be chosen by the script 
    main.py >> the main script that will run the game

Line 1 to 4, we import the modules needed for the game:
    random for using the random.choice to generate a random element from a list
    stages and logo from hangman_art.py file for the art used in the game 
    word_list from hangman_words.py file, for the list of words that we will use to generate a random word 

Line 6 to 9, we set variables as follows: 
    chosen_word - the word that is randomly picked from word_list (imported list from another file)

    display - list holding blank values that will then be swapped with the player's correct guesses (we generate a list of "_" values, multiplied by the length of of the chosen_word variable)

    end_of_game - boolean to hold the status of the game (later changed to True to break out of the while loop when game ends)

    lives - starting number of lives as game begins (we decrement it later when player's guesses are not correct)

Line 11 - we print the logo art that displays at the start of the game

Line 13 to 35 - the main logic of the whole script as follows: 
    Line 13 - the while loop runs as long as the end_of_game is not True

    Line 15 - we take the player's input as lowercase and storing it in the "guess" variable

    Line 17 - we check if their guess is present in the display list (the display list gets populated with correct guesses) and print a confirmation that they already guessed that particular letter

    Line 20 - we iterate through every position in the range of the length of chosen_word for the purpose of populating the display list with player's correct guesses
    
    Line 21 - we assign the value of each specific letter in the chosen_word list, to the letter variable

    Line 22 - we check if the letter variable is the same as the player's guess 

    Line 23 - will set the respective value into the display list, equal to the current letter in the loop, if guess == letter 

    Line 24 - we print the updated display list, after the for loop above is completed, to the player

    Line 25 to 27 - we check the display list for any remaining "_" values and switch the end_of_game to True if 
        none remain, as this means the player guessed all the letters in the chosen_word and then confirm via a print that they won the game
    
    Line 28 to 33 - we check if chosen_word does not contain the guess. If this is true, print a confirmation 
        that they didn't get the guess correctly and that they lost a life, by substracting 1 from the lives variable
        We also check the lives value for when it reaches 0, as this is also another condition for the game to end, and again, here we set the end_of_game variable to True and print to the player that the game was lost
    Line 35 - we print the "status" of the game via an ascii art using the stages list that we imported at the beginning of the script







