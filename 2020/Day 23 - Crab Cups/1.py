from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


with open("input.txt") as fp:
    cups = deque([int(i) for i in fp.read().strip()])


for _ in range(100):
    orig_val = cups[0]
    dest_val = cups[0] - 1
    if dest_val < 1:
        dest_val += 9
    cups.rotate(-1)

    c1 = cups.popleft()
    c2 = cups.popleft()
    c3 = cups.popleft()

    while dest_val in (c1, c2, c3):
        dest_val = dest_val - 1 if dest_val > 1 else dest_val + 8

    while cups[0] != dest_val:
        cups.rotate(-1)
    cups.rotate(-1)

    cups.append(c1)
    cups.append(c2)
    cups.append(c3)

    while cups[0] != orig_val:
        cups.rotate(-1)
    cups.rotate(-1)

while cups[0] != 1:
    cups.rotate(-1)
cups.popleft()

print(''.join([str(i) for i in cups]))
