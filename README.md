Ultimate Texas Hold'em is a 6 player table game played vs the house.
The objective of the game is to have a better hand than the dealer after all five community cards are dealt.
Before recieving their two hole cards, each player places bets on the blind, ante, trips, and progressive.
Progressive and trips are both optional, but have increased payout odds if you hit hands of 3 of a kind or better.
The blind and ante bets are the same size, and usually the minimum is $5. 
After receiving the hole cards, the player can either wager 4x or 3x of their ante on "play", or they can check and see the flop without putting any more money down.
Raising 3x preflop is a -EV play in comparison to 4x or fold, so our strategies will be ignoring that as an option. 
If the player checks pre-flop, they then see a flop of three cards. At this point, they can either check again or bet 2x the ante.
If the player checks again, they then see the turn and river at the same time. At this point, the player can either call (1x ante) or fold.
More playing information and payout structures can be found here:
https://www.pokerlistings.com/how-to-play-ultimate-texas-holdem

This project's goal is to analyze the proper pre-flop 4x range, when to bet 2x on the flop, and when to call river.
This goal includes building an AI Agent, using Reinforcement Learning, that can play GTO.

The game of UTHE is solved statistically knowing only your two cards. You can see analysis at the following links:
https://wizardofodds.com/games/ultimate-texas-hold-em/
https://discountgambling.net/ultimate-texas-holdem/

But, there is a potential (and unproven) player advantage when you know more hands than just your own at the table.
Technically, the rule in UTHE is that you can not share your cards with the table. However, many casinos do not enforce this rule.
Playing six handed with knowledge of all six hands allows the players to check strong hands that you would typically raise with because of blockers from other hands.
A goal of this project is to evaluate the players' edge with this strategy.
Some prior research has been done on this topic:
https://discountgambling.net/2010/01/15/practical-collusion-for-ultimate-texas-holdem/