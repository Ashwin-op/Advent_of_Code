from statistics import median

with open("input.txt") as f:
    values = f.readlines()

mapping = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}
complete_scores = {
    '{': 3,
    '(': 1,
    '[': 2,
    '<': 4
}
line_scores = []

for line in values:
    line = line.strip()
    stack = []
    line_score = 0
    for char in line:
        if char in complete_scores.keys():
            stack.append(char)
        elif len(stack) > 0 and char == mapping[stack[-1]]:
            stack.pop()
        else:
            break
    else:
        # Line is incomplete
        for leftover in reversed(stack):
            line_score *= 5
            line_score += complete_scores[leftover]
        line_scores.append(line_score)

print(median(line_scores))
