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
        str_addr = bin(addr)[2:].zfill(36)
        for addr_str in decode(str_addr, mask):
            mem[int(addr_str, base=2)] = int(val)
print(sum(mem.values()))
