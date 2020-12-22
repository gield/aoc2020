from collections import deque

with open("input.txt", "r") as f:
    raw_decks = [d.strip().split("\n") for d in f.read().split("\n\n")]

deck1, deck2 = [deque(int(c) for c in raw_deck[1:]) for raw_deck in raw_decks]


def play_game(deck1, deck2):
    seen_decks = []
    while deck1 and deck2:
        # Prevent infinite games
        if (deck1, deck2) in seen_decks:
            return deck1.copy(), deque([])
        seen_decks.append((deck1.copy(), deck2.copy()))

        # Each player draws top card
        card1, card2 = deck1.popleft(), deck2.popleft()

        # Check whether the player's deck size >= the card value they draw
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deque(list(deck1)[:card1])
            new_deck2 = deque(list(deck2)[:card2])
            resulting_deck1, resulting_deck2 = play_game(new_deck1, new_deck2)
            player1_won = len(resulting_deck1) > len(resulting_deck2)
        else:
            # The winner of the round is the player with the higher-value card
            player1_won = card1 > card2

        # Place both cards at the bottom of the winner's deck
        if player1_won:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return deck1, deck2


final_deck1, final_deck2 = play_game(deck1, deck2)
winning_deck = reversed(final_deck1 + final_deck2)
print(sum(card * (i + 1) for i, card in enumerate(winning_deck)))
