import random

word_list = ["AARDVARK", "BABOON", "CAMEL"]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

# TODO-1 - Randomly choose a word from the word list.
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while True:
    user_guess = input("Choose a letter: ").upper()
    if user_guess in letters:
        break
    else:
        print("Wrong input, try again.\n")

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if user_guess == letter:
        print(user_guess, end='')
    else:
        print("_", end='')