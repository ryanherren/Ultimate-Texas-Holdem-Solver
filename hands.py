from itertools import combinations

colors = ['heart', 'diamond', 'club', 'spade']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

# Enumerating all possible hands
deck = [Card(value, color) for color in colors for value in values]
hands = list(combinations(deck, 2))

