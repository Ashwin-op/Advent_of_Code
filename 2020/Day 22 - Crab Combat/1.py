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

while p1deck and p2deck:
    p1card = p1deck.pop()
    p2card = p2deck.pop()

    if p1card > p2card:
        p1deck.insert(0, p1card)
        p1deck.insert(0, p2card)
    elif p1card == p2card:
        raise Exception
    else:
        p2deck.insert(0, p2card)
        p2deck.insert(0, p1card)

score = 0
score_factor = 1
if p1deck:
    winner_deck = p1deck
else:
    winner_deck = p2deck

for card in winner_deck:
    score += card * score_factor
    score_factor += 1

print(score)
