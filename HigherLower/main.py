import high_low_art
import game_data
import random

print(high_low_art.logo)


def get_options(options_data):
    """
    :param options_data: list of dictionaries with several instagram accounts. Contains 'name',
    'follower_count' (in millions), 'description', and country.
    :return: option_a, option_b as dictionaries.
    """
    print("Who has more followers on Instagram?")
    option_a, option_b = random.choices(options_data, k=2)
    print(f"Compare A: {option_a['name']}, a {option_a['description'].lower()} from {option_a['country']}.")
    print(high_low_art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description'].lower()} from {option_b['country']}.")
    return option_a, option_b


def game():
    user_score = 0
    option_a, option_b = get_options(game_data.data)
    user_answer = input("Who has more followers on Instagram? Type A or B. ")
