from functools import reduce


with open("input.txt") as fp:
    lines = [i.strip() for i in fp.readlines()]


def evaluate(line):
    while '(' in line:
        last_open = -1
        for i, char in enumerate(line):
            if char == '(':
                last_open = i
            if char == ')':
                simplified = evaluate(line[last_open + 1: i])
                line = line[:last_open] + str(simplified) + line[i + 1:]
                break
    sums = [sum(map(int, segment.split(' + ')))
            for segment in line.split(' * ')]
    return reduce(lambda a, b: a * b, sums)


print(sum(evaluate(line) for line in lines))
