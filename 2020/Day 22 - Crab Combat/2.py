with open("input.txt") as fp:
    data = [i.strip() for i in fp.readlines()]

p1deck = []
p2deck = []
p = 1
for line in data:
    line = line.rstrip('\n')
    if not line:
        p += 1
        continue
    if line.startswith('Player'):
        continue
    if p == 1:
        p1deck.insert(0, int(line))
    else:
        p2deck.insert(0, int(line))


def play_game(p1deck, p2deck):
    prev_states = set()
    while p1deck and p2deck:
        state = (tuple(p1deck), tuple(p2deck))
        if state in prev_states:
            return 1
        prev_states.add(state)

        p1card = p1deck.pop()
        p2card = p2deck.pop()

        winner = None
        if p1card <= len(p1deck) and p2card <= len(p2deck):
            winner = play_game(p1deck[-p1card:].copy(),
                               p2deck[-p2card:].copy())
        elif p1card > p2card:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1deck.insert(0, p1card)
            p1deck.insert(0, p2card)
        elif p1card == p2card:
            raise Exception
        else:
            p2deck.insert(0, p2card)
            p2deck.insert(0, p1card)
    return winner


winner = play_game(p1deck, p2deck)
score = 0
score_factor = 1
if winner == 1:
    winner_deck = p1deck
else:
    winner_deck = p2deck

for card in winner_deck:
    score += card * score_factor
    score_factor += 1

print(score)
