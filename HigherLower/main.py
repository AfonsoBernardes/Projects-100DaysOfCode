import high_low_art
import game_data
import random

print(high_low_art.logo)


def get_options(options_data):
    option_a, option_b = random.choices(options_data, k=2)
    return option_a, option_b


get_options(game_data.data)
