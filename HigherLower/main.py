import high_low_art
import game_data
import random
import os


def get_options(options_data):
    """
    :param options_data: list of dictionaries with several instagram accounts. Contains 'name',
    'follower_count' (in millions), 'description', and country.
    :return: option_a, option_b as dictionaries.
    """
    print(f"Current score: {user_score}")
    # So that the same account is not compared with itself.
    option_b = random.choice(options_data)
    while option_a == option_b:
        option_b = random.choice(options_data)
    print(f"Compare A: {option_a['name']}, a {option_a['description'].lower()} from {option_a['country']}.")
    print(high_low_art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description'].lower()} from {option_b['country']}.\n")
    return option_a, option_b


def check_input(option_a, option_b):
    """
    Check if user input is 'A' or 'B'.
    :return: boolean if user choice has more followers than the other option.
    """
    while True:
        user_answer = input("Who has more followers on Instagram? Type A or B. ").upper()
        if user_answer == 'A':
            return option_a['follower_count'] > option_b['follower_count']
        elif user_answer == 'B':
            return option_b['follower_count'] > option_a['follower_count']
        else:
            print("Invalid input. Try again.")


def game(score):
    option_a, option_b = get_options(game_data.data)
    if check_input(option_a, option_b):
        score += 1
        return True, score, option_a, option_b
    else:
        return False, score, option_a, option_b


keep_playing = True
user_score = 0
# Initialise options so that we can swap them even the first time.
option_a = random.choice(game_data.data)
option_b = random.choice(game_data.data)
while keep_playing:
    # This line clears screen. If not working, check IDE configs and toggle "Emulate terminal in output console".
    os.system('cls')
    print(high_low_art.logo)
    # Make option_a be option_b to prevent the game to get stuck on most followed account. These are global variables.
    option_a = option_b
    keep_playing, user_score, option_a, option_b = game(score=user_score)

print(f"Sorry, that's wrong. Final score: {user_score}.")
