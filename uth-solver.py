import numpy as np
# import pied_poker as pp
from math import comb
from itertools import combinations
import random
from treys import Evaluator, Deck
from treys import Card as cd
import time
from datetime import datetime

connectors = [['A','2'], ['2','3'], ['3','4'], ['4','5'], ['5','6'], ['6','7'], ['7','8'], ['8','9'], ['9','T'], ['T','J'], ['J','Q'], ['Q','K'], ['K','A']]
colors = ['heart', 'diamond', 'club', 'spade']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
broadways = ['A', 'K', 'Q', 'J', 'T']
sort_order = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12, '2': 13}

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
        self.broadway = True if self.high in broadways and self.low in broadways and self.high != self.low else False
        self.suited_broadway = self.suited and self.broadway
        self.connecter = True if [self.low, self.high] in connectors else False    
        self.suited_connector = True if [self.low, self.high] in connectors and self.suited else False
        self.pair_odds = 100 if self.pair else 0
        self.two_pair_odds = 0
        self.set_odds = 0
        self.straight_odds = 0
        self.flush_odds = 0
        self.full_house_odds = 0
        self.quads_odds = 0
        self.straight_flush_odds = 0
        self.royal_flush_odds = 0

def start_hand():
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

    pair_odds = ()
    return pair_outs

def calculate_combinations(deck, cards):
    return comb(len(deck), cards)

def get_community_cards(deck, num_cards):
    community = []
    for i in range(num_cards):
        community.append(deck.pop())
    return community

def check_hand(end_hand):
    print("Checking hand: ", end_hand)

def check_high_card(hand):
    maxi = max(hand[0].value, hand[1].value, hand[2].value, hand[3].value, hand[4].value, hand[5].value)
    return maxi

def sort_hand(hand):
    hand.sort(key=lambda card: sort_order[card.value])
    return hand

# Get the deck and the table
deck = start_hand()
NUM_PLAYERS = 6
table = get_table(deck, NUM_PLAYERS)

# Get the hands
hands =[]
for i in range(NUM_PLAYERS):
    hands.append(Hand(table[i]))

# Get all other possible hands
other_hands2 = list(combinations(deck, 2))
other_hands = []
for hand in other_hands2:
    other_hands.append(Hand(hand))
print(len(other_hands))

# for hand in hands:
#     if not hand.pair:
#         hand.pair_odds = calculate_pair(hand, deck)

# for hand in hands:
#     print(hand.pair_odds)

# Print each hand and its attributes
# for hand in hands:
#     print(hand.hand[0].value, hand.hand[0].suit, hand.hand[1].value, hand.hand[1].suit)
#     print(hand.pair, hand.suited, hand.high, hand.low, hand.broadway, hand.suited_broadway, hand.connecter, hand.suited_connector)

# print("Table cards: ")
# # Print the table cards 
# for i in range(NUM_PLAYERS):
#     print(table[i][0].value, table[i][0].suit, table[i][1].value, table[i][1].suit)

community_cards = get_community_cards(deck, 5)

# print("Community cards: ")
# # Print the community cards
# for i in range(5):
#     print(community_cards[i].value, community_cards[i].suit)

# print("-------------------")

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

# print("Community combinations: ", calculate_combinations(deck, 5))

# Creating ending hands including community cards. This is an array of 7 card arrays
end_hands = []
temp_hand = []
for hand in hands:
    for card in hand.hand:
        # print("Appending player: ", card.value, card.suit)
        temp_hand.append(card)
    for card in community_cards:
        # print("Appending com: ", card.value, card.suit)
        # print(card.value, card.suit)
        temp_hand.append(card)
    end_hands.append(Hand(temp_hand))
    temp_hand = []
    # end_hands.append(hand.hand, community_cards)

# Creating clean hands for each hand in format of ValueSuit, ValueSuit, ValueSuit, ValueSuit, ValueSuit, ValueSuit, ValueSuit
# For example, a hand with ['A', 'heart'], ['K', 'heart'], ['Q', 'heart'], ['J', 'heart'], ['T', 'heart'], ['9', 'heart'], ['8', 'heart'] will be printed as:
# [Ah, Kh, Qh, Jh, Th, 9h, 8h]
# For use in treys evaluator
# First, for the hands
card_str = ""
card_list = []
# Hand_list has hands for all NUM_PLAYERS players
hand_list = []
for hand in hands:
    for card in hand.hand:
        val = card.value
        suit = card.suit[0]
        # print("Val: ", val, "Suit: ", suit)
        card_str += val + suit
        c = cd.new(card_str)
        card_list.append(c)
        card_str = ""
    hand_list.append(card_list)
    card_list = []
# Then, for the community cards
board = []
for card in community_cards:
    val = card.value
    suit = card.suit[0]
    print("Val: ", val, "Suit: ", suit)
    card_str += val + suit
    c = cd.new(card_str)
    board.append(c)
    card_str = ""
# Then, for all possible hands
# how to access: other_hands[0][0].value, other_hands[0][0].suit, other_hands[0][1].value, other_hands[0][1].suit
# This is every other possible hand (780) when taking out the player hands and the community cards
# There is a bug somewhere in here (probably with assigning card_str) that causes flushes to break in evaluation
all_hands = []
card_list2 = []
for hand in other_hands:
    for card in hand.hand:
        val = card.value
        suit = card.suit[0]
        # print("Val: ", val, "Suit: ", suit)
        card_str += val + suit
        # print(card_str)
        c = cd.new(card_str)
        card_list2.append(c)
        card_str = ""
    all_hands.append(card_list2)
    card_list2 = []

# now = datetime.now()
# file_name = "all_hands" + now.strftime("%Y%m%d%H%M%S") + ".csv"
# np.savetxt(file_name, all_hands, delimiter=",", fmt='%s')
# Printing all ending hands
# for hand in end_hands:
#     print(hand.hand[0].value, hand.hand[0].suit, hand.hand[1].value, hand.hand[1].suit, hand.hand[2].value, hand.hand[2].suit, hand.hand[3].value, hand.hand[3].suit, hand.hand[4].value, hand.hand[4].suit, hand.hand[5].value, hand.hand[5].suit, hand.hand[6].value, hand.hand[6].suit)

# for hand in end_hands:
#     for card in hand:
#         print(card.value, card.suit)
#     print("--------")
evaluator = Evaluator()

# Evaluate all other possible hands without community cards and player cards
all_scores = []
all_classes = []
for hand in all_hands:
    # time.sleep(0.1)
    score = evaluator.evaluate(hand, board)
    all_scores.append(score)
    class_ = evaluator.get_rank_class(score)
    all_classes.append(class_)
    # cd.print_pretty_cards(hand)
    # print("Score: %d - %s" % (score, evaluator.class_to_string(class_)))


# Print all treys formatted hands
scores = []
classes = []
print("Board: ")
cd.print_pretty_cards(board)
print("-------------------")
for hand in hand_list:
    score = evaluator.evaluate(hand, board)
    scores.append(score)
    class_ = evaluator.get_rank_class(score)
    classes.append(class_)
    cd.print_pretty_cards(hand)
    print("Score: %d - %s" % (score, evaluator.class_to_string(class_)))
# print(evaluator.evaluate(hand_list[0], board))

# Counting number of winning hands for each player
num_hands = len(all_scores)
num_winning_hands = []
for score in scores:
    winning_hands = 0
    for score2 in all_scores:
        if score < score2:
            winning_hands += 1
    num_winning_hands.append(winning_hands)

for i in range(len(num_winning_hands)):
    print("Player ", i+1, " wins ", num_winning_hands[i], " hands out of ", num_hands, " hands, which is ", num_winning_hands[i]/num_hands*100, "%")

# # Print ending hand 1
# print("-------------------")
# print("End hand 1: ")
# for card in end_hands[0].hand:
#     print(card.value, card.suit)

# # Print sorted ending hand 1
# sorted_end_hand = sort_hand(end_hands[0].hand)
# print("Sorted end hand 1: ")
# for card in sorted_end_hand:
#     print(card.value, card.suit)
