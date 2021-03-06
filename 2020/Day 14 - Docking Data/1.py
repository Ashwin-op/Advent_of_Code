from collections import defaultdict


with open("input.txt") as fp:
    lines = [i.strip().split(' = ') for i in fp.readlines()]


def decode(addr: str, mask: str, bit: int = 0):
    if bit < 35:
        if mask[bit] == "0":
            for rest in decode(addr, mask, bit + 1):
                yield addr[bit] + rest
        elif mask[bit] == "1":
            for rest in decode(addr, mask, bit + 1):
                yield "1" + rest
        elif mask[bit] == "X":
            for rest in decode(addr, mask, bit + 1):
                yield "0" + rest
                yield "1" + rest
    else:
        if mask[bit] == "0":
            yield addr[bit]
        elif mask[bit] == "1":
            yield "1"
        elif mask[bit] == "X":
            yield "0"
            yield "1"


mask = ""
mem = defaultdict(int)
for lval, val in lines:
    if lval == "mask":
        mask = val
    else:
        addr = int(lval[4:-1])
        str_val = bin(int(val))[2:].zfill(36)
        mem[addr] = int(
            "".join(
                bit if mask_bit == "X" else mask_bit
                for bit, mask_bit in zip(str_val, mask)
            ),
            base=2,
        )
print(sum(mem.values()))