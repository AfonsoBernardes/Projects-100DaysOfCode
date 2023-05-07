import pandas as pd

# Create a dictionary in this format:
df_nato = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df_nato.iterrows()}


def generate_phonetic_message():
    # Create a list of the phonetic code words from a word that the user inputs. Accept sentences.
    user_input = input("Write a word to translate into the NATO alphabet. ")
    # nato_list = [nato_dict[letter.upper()] if letter.upper() in nato_dict else letter for letter in user_input]
    try:
        nato_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print(f"Sorry, only letters of the alphabet are allowed: no numbers, symbols or spaces. Try again.\n")
        generate_phonetic_message()
    else:
        print(nato_list)


generate_phonetic_message()
