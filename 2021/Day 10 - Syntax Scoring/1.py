with open("input.txt") as f:
    values = f.readlines()

mapping = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}
scores = {
    '}': 1197,
    ')': 3,
    ']': 57,
    '>': 25137
}
corrupt_score = 0

for line in values:
    line = line.strip()
    stack = []
    for char in line:
        if char in ['{', '(', '[', '<']:
            stack.append(char)
        elif len(stack) > 0 and char == mapping[stack[-1]]:
            stack.pop()
        else:
            corrupt_score += scores[char]
            break

print(corrupt_score)
