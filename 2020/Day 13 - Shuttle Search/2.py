with open("input.txt") as fp:
    _ = int(fp.readline().strip())
    busTimes = fp.readline().split(',')


def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total


pairs = []
for i, n in enumerate(busTimes):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n - i, n))
print(crt(pairs))
