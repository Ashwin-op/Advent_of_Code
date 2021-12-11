with open('input.txt') as f:
    segments = [
        (left.split(), right.split())
        for line in f.readlines()
        for left, right in [line.split(" | ")]
    ]

known = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

print(sum(len(seq) in known for line in segments for seq in line[1]))
