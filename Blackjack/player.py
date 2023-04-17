class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        print(f"{self.name}'s hand:", end=" ")
        for card in self.hand:
            card.show_card()
        print("")
