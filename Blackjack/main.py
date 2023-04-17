from blackjack_ascii import logo
import deck
import player

############### Simplified Blackjack #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The  Ace can count as 11 or 1.
# Use the following list as the deck of cards: [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
# The cards in the list have equal probability of being drawn.
# The computer is the dealer.

print(logo)

# Create and shuffle deck before game starts.
deck = deck.Deck()
deck.shuffle()
play_game = True

# Only one player for now, scalable later...
player_name = input("Hello, welcome to Blackjack. What is your name? ")
user = player.Player(name=player_name)
dealer = player.Player(name='Dealer')

while play_game:
    user.draw_card(deck)
    dealer.draw_card(deck)
    user.draw_card(deck)
    dealer.draw_card(deck)
    play_game = False

user.show_hand()
dealer.show_hand()

