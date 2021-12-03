from itertools import islice, tee


def pairwise(iterable, offset=1):
    a, b = tee(iterable)
    return zip(a, islice(b, offset, None))


def compare(numbers, n):
    return sum(x < y for x, y in pairwise(numbers, offset=n))


with open("input.txt") as fp:
    numbers = [int(line.strip()) for line in fp.readlines()]

    print(compare(numbers, 3))
