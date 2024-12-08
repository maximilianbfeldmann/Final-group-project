# Pack zum Mischen der Karten
import random


# Kartendeck und Werte
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Deck mischen
random.shuffle(deck)

# Oberste Karte vom Deck ziehen
def deal_card(deck):
    return deck.pop()

# Hand zählen
def calculate_total(hand):
    total = sum(card_values[card] for card in hand)
    # Ass als 1 ausgeben wenn Busted
    for card in hand:
        if card == 'A' and total > 21:
            total -= 10
    return total

# Spielzug Spieler
def player_turn(deck, player_hand):
    while True:
        player_choice = input("Ziehen oder Bleiben? ").lower()
        if player_choice == 'ziehen':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Deine Hand:", player_hand, "Summe:", total)
            if total > 21:
                print("Oh Nein! Du hast verloren. Dein Geld gehört mir!")
                return False
        elif player_choice == 'bleiben':
            return True

# Spielzug Dealer
def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    return dealer_hand

# Blackjack Spiel
while True:
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("Deine Hand:", player_hand, "Summe:", calculate_total(player_hand))
    print("Dealer's Hand:", dealer_hand[0])

    # Spieler am Zug
    if player_turn(deck, player_hand):
        dealer_hand = dealer_turn(deck, dealer_hand)
        print("Dealer's Hand:", dealer_hand, "Summe:", calculate_total(dealer_hand))
       
        # Gewinner festlegen
        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)
        if player_total > dealer_total:
            print("Du hast gewonnen!")
        elif dealer_total > 21:
            print("Dealer hat sich überkauft! Du gewinnst!")
        elif dealer_total > player_total:
            print("Dealer gewinnt!")
        else:
            print("Unentschieden!")

    # Zweite Runde anbieten
    play_again = input("Nochmal spielen? (Ja/Nein): ").lower()
    if play_again != 'ja':
        break

    # Deck neu anlegen und mischen
    if len(deck) < 10:
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)

print("Danke fürs mitspielen!")
