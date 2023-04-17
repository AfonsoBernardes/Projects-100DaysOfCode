class Card:
    suits = {
        'Spades': "♠",
        'Hearts': "♥",
        'Diamonds': "♦",
        'Clubs': "♣",
    }

    def __init__(self, rank: str, suit: str, value: int):
        self.rank = rank  # '2', '3', ..., 'K', 'A'
        self.value = value  # 2, 3, ..., 10, 10, 11
        self.suit = self.suits[suit]

    def show_card(self):
        print(f"{self.rank}{self.suit}")
