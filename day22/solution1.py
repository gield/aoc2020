from collections import deque

with open("input.txt", "r") as f:
    raw_decks = [d.strip().split("\n") for d in f.read().split("\n\n")]

deck1, deck2 = [deque(int(c) for c in raw_deck[1:]) for raw_deck in raw_decks]

while deck1 and deck2:
    card1, card2 = deck1.popleft(), deck2.popleft()
    if card1 > card2:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])

winning_deck = reversed(deck1 + deck2)
print(sum(card * (i + 1) for i, card in enumerate(winning_deck)))
