import pandas as pd

# Create a dictionary in this format:
df_nato = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df_nato.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs. Accept sentences.
user_input = input("Write a word to translate into the NATO alphabet. ")
nato_list = [nato_dict[letter.upper()] if letter.upper() in nato_dict else letter for letter in user_input]
print(nato_list)
