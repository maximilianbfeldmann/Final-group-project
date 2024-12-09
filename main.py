import random

# Kartendeck und Werte
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

# Karten-ASCII-Art
card_art = {
    '2':  ["┌─────────┐", "│2        │", "│         │", "│    ♦    │", "│         │", "│        2│", "└─────────┘"],
    '3':  ["┌─────────┐", "│3        │", "│         │", "│  ♦ ♦ ♦  │", "│         │", "│        3│", "└─────────┘"],
    '4':  ["┌─────────┐", "│4        │", "│  ♦   ♦  │", "│         │", "│  ♦   ♦  │", "│        4│", "└─────────┘"],
    '5':  ["┌─────────┐", "│5        │", "│  ♦   ♦  │", "│    ♦    │", "│  ♦   ♦  │", "│        5│", "└─────────┘"],
    '6':  ["┌─────────┐", "│6        │", "│  ♦   ♦  │", "│  ♦   ♦  │", "│  ♦   ♦  │", "│        6│", "└─────────┘"],
    '7':  ["┌─────────┐", "│7        │", "│  ♦   ♦  │", "│  ♦   ♦  │", "│  ♦   ♦  │", "│        7│", "└─────────┘"],
    '8':  ["┌─────────┐", "│8        │", "│ ♦   ♦   │", "│  ♦   ♦  │", "│ ♦   ♦   │", "│        8│", "└─────────┘"],
    '9':  ["┌─────────┐", "│9        │", "│ ♦   ♦   │", "│ ♦   ♦   │", "│ ♦   ♦   │", "│        9│", "└─────────┘"],
    '10': ["┌─────────┐", "│10       │", "│ ♦   ♦   │", "│  ♦   ♦  │", "│ ♦   ♦   │", "│       10│", "└─────────┘"],
    'J':  ["┌─────────┐", "│J        │", "│         │", "│    ♠    │", "│         │", "│        J│", "└─────────┘"],
    'Q':  ["┌─────────┐", "│Q        │", "│         │", "│    ♠    │", "│         │", "│        Q│", "└─────────┘"],
    'K':  ["┌─────────┐", "│K        │", "│         │", "│    ♠    │", "│         │", "│        K│", "└─────────┘"],
    'A':  ["┌─────────┐", "│A        │", "│         │", "│    ♠    │", "│         │", "│        A│", "└─────────┘"],
    '?':  ["┌─────────┐", "│░░░░░░░░░│", "│░░░░░░░░░│", "│░░░░░░░░░│", "│░░░░░░░░░│", "│░░░░░░░░░│", "└─────────┘"]
}

# Funktion zur Darstellung der Karten in ASCII-Art
def print_hand(hand):
    lines = [""] * 7
    for card in hand:
        art = card_art[card]
        for i, line in enumerate(art):
            lines[i] += line + "  "
    print("\n".join(lines))

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
        print("\nDeine Hand:")
        print_hand(player_hand)
        print(f"Summe: {calculate_total(player_hand)}")
        player_choice = input("Ziehen oder Bleiben? ").lower()
        if player_choice == 'ziehen':
            player_hand.append(deal_card(deck))
            if calculate_total(player_hand) > 21:
                print("\nOh Nein! Du hast verloren. Dein Geld gehört mir!")
                print_hand(player_hand)
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
    
    print("\nDealer's Hand:")
    print_hand([dealer_hand[0], '?'])  # Erste Karte verdeckt

    # Spieler am Zug
    if player_turn(deck, player_hand):
        # Dealer am Zug
        dealer_hand = dealer_turn(deck, dealer_hand)
        print("\nDealer's Hand:")
        print_hand(dealer_hand)
        print(f"Summe: {calculate_total(dealer_hand)}")
       
        # Gewinner festlegen
        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)
        if player_total > dealer_total or dealer_total > 21:
            print("\nDu hast gewonnen!")
        elif dealer_total > player_total:
            print("\nDealer gewinnt!")
        else:
            print("\nUnentschieden!")

    # Zweite Runde anbieten
    play_again = input("\nNochmal spielen? (Ja/Nein): ").lower()
    if play_again != 'ja':
        break

    # Deck neu anlegen und mischen
    if len(deck) < 10:
        deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(deck)

print("\nDanke fürs mitspielen!")
