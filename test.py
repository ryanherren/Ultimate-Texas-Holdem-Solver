from treys import Evaluator, Deck
from treys import Card as cd

board = [cd.new('Ah'), cd.new('Kd'), cd.new('Qs'), cd.new('Jh'), cd.new('Th')]
hand = [cd.new('9h'), cd.new('8h')]

evaluator = Evaluator()
score = evaluator.evaluate(hand, board)
print(score, evaluator.class_to_string(evaluator.get_rank_class(score)))
cd.print_pretty_cards(board + hand)