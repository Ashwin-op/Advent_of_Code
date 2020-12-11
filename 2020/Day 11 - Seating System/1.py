from copy import deepcopy


with open("input.txt") as fp:
    data = [list(line) for line in fp.read().splitlines()]


def is_same(old, new):
    for i in range(len(old)):
        for j in range(len(old[i])):
            if old[i][j] != new[i][j]:
                return False
    return True


def count(l):
    c = 0
    for i in l:
        for j in i:
            if j == "#":
                c += 1
    return c


def solve():
    s = deepcopy(data)
    while True:
        n = deepcopy(s)

        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == '.':
                    continue

                o = 0
                if i > 0:
                    if j > 0 and s[i-1][j-1] == '#':
                        o += 1
                    if s[i-1][j] == '#':
                        o += 1
                    if j+1 < len(s[i-1]) and s[i-1][j+1] == '#':
                        o += 1
                if j > 0 and s[i][j-1] == '#':
                    o += 1
                if j+1 < len(s[i]) and s[i][j+1] == '#':
                    o += 1
                if i+1 < len(s):
                    if j > 0 and s[i+1][j-1] == '#':
                        o += 1
                    if s[i+1][j] == '#':
                        o += 1
                    if j+1 < len(s[i+1]) and s[i+1][j+1] == '#':
                        o += 1

                if o == 0:
                    n[i][j] = '#'
                elif o >= 4:
                    n[i][j] = 'L'

        if is_same(s, n):
            return count(n)
        else:
            s = n


print(solve())
