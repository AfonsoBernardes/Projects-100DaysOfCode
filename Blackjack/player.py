class Player:
    def __init__(self, name):
        self.current_score = 0
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def has_ace(self):
        """
        Check if player has an Ace on his hand.
        :return: boolean
        """
        for card in self.hand:
            if card.rank == 'A':
                return True
        return False

    def get_ace_11(self):
        """
        Find (in hand) ace with value equals to 11.
        :return: card object
        """
        for card in self.hand:
            if card.rank == 'A' and card.get_value() == 11:
                return card

    def get_hand_score(self):
        self.current_score = 0
        for card in self.hand:
            if card.get_is_face_up():
                self.current_score += card.get_value()
        return self.current_score

    def show_hand(self):
        print(f"{self.name}'s hand:", end=" ")
        for card in self.hand:
            card.show_card()
        print(f"(Current hand value: {self.get_hand_score()})")
