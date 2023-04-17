import card
import random


class Deck:
    """
    Create a deck of 52 cards.
    """
    card_dict = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for rank, value in self.card_dict.items():
                self.cards.append(card.Card(rank=rank, suit=s, value=value))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)
