from treys import Evaluator, Deck
from treys import Card as cd

# This is worst possible pair, so every hand ranking less than or equal to this
# means that the dealer has qualified. Rating is 6168
board = [cd.new('2h'), cd.new('2d'), cd.new('3s'), cd.new('4h'), cd.new('5d')]
hand = [cd.new('8s'), cd.new('7c')]

evaluator = Evaluator()
score = evaluator.evaluate(hand, board)
print(score, evaluator.class_to_string(evaluator.get_rank_class(score)))
cd.print_pretty_cards(board + hand)