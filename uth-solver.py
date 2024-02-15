import numpy as np
# import pied_poker as pp
from math import comb

connectors = [['A','2'], ['2','3'], ['3','4'], ['4','5'], ['5','6'], ['6','7'], ['7','8'], ['8','9'], ['9','T'], ['T','J'], ['J','Q'], ['Q','K'], ['K','A']]

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.pair = hand[0].value == hand[1].value
        self.suited = hand[0].suit == hand[1].suit
        self.high = max(hand[0].value, hand[1].value)
        self.low = min(hand[0].value, hand[1].value)
        self.broadway = True if self.high in ['A', 'K', 'Q', 'J', 'T'] and self.low in ['A', 'K', 'Q', 'J', 'T'] and self.high != self.low else False
        self.suited_broadway = self.suited and self.broadway
        self.connecter = True if [self.low, self.high] in connectors else False    
        self.suited_connector = True if [self.low, self.high] in connectors and self.suited else False
        self.pair_odds = 0
        self.two_pair_odds = 0
        self.set_odds = 0
        self.straight_odds = 0
        self.flush_odds = 0
        self.full_house_odds = 0
        self.quads_odds = 0
        self.straight_flush_odds = 0
        self.royal_flush_odds = 0

def start_hand():
    colors = ['heart', 'diamond', 'club', 'spade']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [Card(value, color) for color in colors for value in values]
    np.random.shuffle(deck)
    return deck

def get_hand(deck):
    hand = []
    for i in range(2):
        hand.append(deck.pop())
    return Hand(hand)

def get_table(deck, players):
    table = []
    hand = []
    for i in range(players):
        hand.append(deck.pop())
        hand.append(deck.pop())
        table.append(hand)
        hand = []
    return table

def calculate_pair(hand, deck):
    pair_outs = 0
    for card in deck:
        if card.value == hand.high or card.value == hand.low:
            pair_outs += 1
    return pair_outs

def calculate_combinations(deck, cards):
    return comb(len(deck), cards)


# Get the deck and the table
deck = start_hand()
NUM_PLAYERS = 6
table = get_table(deck, NUM_PLAYERS)

hands =[]
for i in range(NUM_PLAYERS):
    hands.append(Hand(table[i]))

# Print each hand and its attributes
for hand in hands:
    print(hand.hand[0].value, hand.hand[0].suit, hand.hand[1].value, hand.hand[1].suit)
    print(hand.pair, hand.suited, hand.high, hand.low, hand.broadway, hand.suited_broadway, hand.connecter, hand.suited_connector)

# Print the table cards 
for i in range(NUM_PLAYERS):
    print(table[i][0].value, table[i][0].suit, table[i][1].value, table[i][1].suit)



# print(hand.hand[0].value, hand.hand[0].suit, hand.hand[1].value, hand.hand[1].suit)
# # print("pair: ", hand.pair, "suited: ", hand.suited, "high: ", hand.high, "low: ", hand.low, "broadway: ", hand.broadway, "suited_broadway: ", hand.suited_broadway, "suited_connector: ", hand.suited_connector)
# print("High: ", hand.high)
# print("Low: ", hand.low)
# print("Pair: ", hand.pair)
# print("Suited: ", hand.suited)
# print("Broadway: ", hand.broadway)
# print("Suited Broadway: ", hand.suited_broadway)
# print("Connector: ", hand.connecter)
# print("Suited Connector: ", hand.suited_connector)

# print("Deck length: ", len(deck))
# print("Pair outs: ", calculate_pair(hand, deck))

print("Community combinations: ", calculate_combinations(deck, 5))





