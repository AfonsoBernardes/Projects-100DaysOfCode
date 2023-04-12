import os
import random
from hangman_ascii_art import stages_ascii, logo
from hangman_word_list import word_list

print(logo)
word_list = word_list
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

# Randomly choose a word from the word list. For each letter in the chosen_word, add a "_" to a list.
chosen_word = random.choice(word_list).upper()
display = ['_' for idx in range(len(chosen_word))]
letters_guessed = []

# Ask the user to guess a letter. Wrap code in a while loop to let the user guess again.
lives_left = 6
end_of_game = "_" not in display
while not end_of_game:
    while True:
        user_guess = input("Choose a letter: ").upper()
        # This line clears screen to prevent too much scrolling. If not working, check IDE configs and toggle
        # "Emulate terminal in output console".
        os.system('cls')
        if user_guess in letters:
            # Store letters that user introduces to warn her/him if repeated letter is chosen.
            if user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                break
            else:
                print("You already tried that letter. Go again.")
        else:
            print("Wrong input, try again.\n")

    # Check if the letter the user guessed is one of the letters in the chosen_word. If user guesses a letter that
    # exists, replace "_" with the letter in the display list.
    if user_guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if user_guess == letter:
                display[idx] = user_guess
    else:
        lives_left -= 1

    print(' '.join(display))
    print(stages_ascii[lives_left])
    end_of_game = "_" not in display or lives_left == 0

if lives_left == 0:
    print("YOU LOSE!")
else:
    print("CONGRATULATIONS, YOU WON")
