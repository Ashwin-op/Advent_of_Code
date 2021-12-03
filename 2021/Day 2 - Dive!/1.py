MOVEMENTS = {
    'forward': lambda x, y, a: (x + a, y),
    'down': lambda x, y, a: (x, y - a),
    'up': lambda x, y, a: (x, y + a),
}


with open("input.txt") as fp:
    movements = []
    for line in fp.readlines():
        direction, amount = line.strip().split()
        movements.append((direction, int(amount)))

    x, y = 0, 0
    for direction, amount in movements:
        x, y = MOVEMENTS[direction](x, y, amount)

    print(abs(x) * abs(y))
