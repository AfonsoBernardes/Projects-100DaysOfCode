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

# ace = card.Card(rank='A', value=11, suit="Spades", face_up=True)

while play_game:
    # This is the initial hand. Dealer's second card is hidden.
    user.draw_card(deck)
    # user.hand.append(ace)
    dealer.draw_card(deck)
    user.draw_card(deck)
    dealer.draw_card(deck)
    dealer.hand[-1].set_is_face_up(face_up=False)

    user.show_hand()
    dealer.show_hand()

    # If player has blackjack from the start, do not enter loop.
    if user.get_hand_score() == 21:
        print("You have blackjack!")
    else:
        # PLAYER'S LOOP
        player_not_bust = True
        while player_not_bust:
            while True:
                user_action = input("\nDo you want to HIT or STAND? ").upper()
                if user_action == 'HIT' or user_action == 'STAND':
                    break
                else:
                    print('Invalid action, try again.')

            if user_action == 'HIT':
                user.draw_card(deck)
                # When player hits and hand's score is above 21, check for aces with value=11 and replace for value=1.
                if user.is_bust() and user.get_ace_11() is not None:
                    user.get_ace_11().set_value(1)
                    user.show_hand()
                    dealer.show_hand()

                # Player's hand over 21 without an ace to change.
                elif user.is_bust():
                    player_not_bust = False
                    user.show_hand()
                    dealer.show_hand()
                    print("BUST! YOU LOSE!\n")
                    break

                # Simply display hands after hitting.
                else:
                    user.show_hand()
                    dealer.show_hand()
            # Break player's loop and move to dealer's.
            elif user_action == 'STAND':
                break

    # Flip dealer's card up
    dealer.hand[-1].set_is_face_up(face_up=True)
    user.show_hand()
    dealer.show_hand()
    print("")
    if player_not_bust:
        while dealer.get_hand_score() < 17:
            dealer.draw_card(deck)

            if dealer.is_bust() and dealer.get_ace_11() is not None:
                dealer.get_ace_11().set_value(1)
                user.show_hand()
                dealer.show_hand()
                print("")

            elif dealer.is_bust():
                user.show_hand()
                dealer.show_hand()
                print("YOU WIN!")  # Here already implies that player is not bust.
                break

            else:
                user.show_hand()
                dealer.show_hand()
                print("")

    play_game = False
