from collections import Counter


with open("input.txt") as fp:
    adapters = sorted([int(i.strip()) for i in fp.readlines()])
    adapters = [0] + adapters + [adapters[-1] + 3]

diffs = Counter([y - x for x, y in zip(adapters, adapters[1:])])
print(diffs[1] * diffs[3])
