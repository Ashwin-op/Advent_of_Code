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
    vals = line.split(' ')
    op = None
    total = int(vals[0])
    for val in vals[1:]:
        if val == '+':
            def op(a, b): return a + b
        elif val == '*':
            def op(a, b): return a * b
        else:
            total = op(total, int(val))
    return total


print(sum(evaluate(line) for line in lines))
