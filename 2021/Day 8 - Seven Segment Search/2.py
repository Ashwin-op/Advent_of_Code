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


def decode_line(left, right):
    num_map = {
        known[len(seq)]: frozenset(seq) for seq in left if len(seq) in known
    }
    n2_3_5 = {frozenset(seq) for seq in left if len(seq) == 5}
    n0_6_9 = {frozenset(seq) for seq in left if len(seq) == 6}
    num_map[3] = next(s for s in n2_3_5 if len(num_map[1] & s) == 2)
    num_map[2] = next(s for s in n2_3_5 -
                      {num_map[3]} if len(num_map[4] | s) == 7)
    num_map[5] = next(iter(n2_3_5 - {num_map[3], num_map[2]}))
    num_map[9] = next(s for s in n0_6_9 if len(num_map[3] | s) == len(s))
    num_map[0] = next(s for s in n0_6_9 -
                      {num_map[9]} if len(num_map[1] & s) == 2)
    num_map[6] = next(iter(n0_6_9 - {num_map[9], num_map[0]}))

    set_to_num = {s: f"{n}" for n, s in num_map.items()}

    return int("".join(set_to_num[frozenset(seq)] for seq in right))

print(sum(decode_line(*line) for line in segments))
