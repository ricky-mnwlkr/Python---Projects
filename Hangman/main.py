import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
  
chosen_word = random.choice(word_list)
display = ['_'] * (len(chosen_word))
end_of_game = False
lives = 6

print(logo)

while not end_of_game:

    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter: 
            display[position] = letter 
    print(''.join(display))
    if '_' not in display:
        end_of_game = True
        print('You win the game!')
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f'You lose.')
    
    print(stages[lives])
    
























