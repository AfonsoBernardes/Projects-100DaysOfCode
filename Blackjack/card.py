class Card:
    suits = {
        'Spades': "♠",
        'Hearts': "♥",
        'Diamonds': "♦",
        'Clubs': "♣",
    }

    def __init__(self, rank: str, suit: str, value: int, face_up=True):
        self.rank = rank  # '2', '3', ..., 'K', 'A'
        self.value = value  # 2, 3, ..., 10, 10, 11
        self.suit = self.suits[suit]
        self.face_up = face_up

    # Setter and getter for face up/down card.
    def get_is_face_up(self):
        return self.face_up

    def set_is_face_up(self, face_up: bool):
        self.face_up = face_up

    # Setter and getter for card value. Should restrain changing value unless is an Ace.
    def get_value(self):
        return self.value

    def set_value(self, value: int):
        self.value = value

    def show_card(self):
        if self.get_is_face_up():
            print(f"{self.rank}{self.suit}", end=" ")
        else:
            print(f"?{self.suit}", end=" ")
