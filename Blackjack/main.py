from blackjack_ascii import logo
import deck

############### Simplified Blackjack #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The  Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

print(logo)
deck = deck.Deck()
deck.shuffle()
deck.show_deck()
deck.draw_card().show_card()


