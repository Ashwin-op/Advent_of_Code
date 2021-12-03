MOVEMENTS = {
    'forward': lambda x, y, aim, a: (x + a, y + aim * a, aim),
    'down': lambda x, y, aim, a: (x, y, aim + a),
    'up': lambda x, y, aim, a: (x, y, aim - a),
}


with open("input.txt") as fp:
    movements = []
    for line in fp.readlines():
        direction, amount = line.strip().split()
        movements.append((direction, int(amount)))

    x, y, aim = 0, 0, 0
    for movement in movements:
        x, y, aim = MOVEMENTS[movement[0]](x, y, aim, movement[1])

    print(abs(x) * abs(y))
