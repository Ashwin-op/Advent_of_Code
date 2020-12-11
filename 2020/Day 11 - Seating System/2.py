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
    c = 0
    while True:
        c += 1
        n = deepcopy(s)

        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == '.':
                    continue

                z = 0

                o = 0
                while True:
                    o += 1
                    if i-o >= 0 and j-o >= 0:
                        if s[i-o][j-o] == '#':
                            z += 1
                            break
                        elif s[i-o][j-o] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if i-o >= 0:
                        if s[i-o][j] == '#':
                            z += 1
                            break
                        elif s[i-o][j] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if i-o >= 0 and j+o < len(data[0]):
                        if s[i-o][j+o] == '#':
                            z += 1
                            break
                        elif s[i-o][j+o] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if j+o < len(data[0]):
                        if s[i][j+o] == '#':
                            z += 1
                            break
                        elif s[i][j+o] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if i+o < len(data) and j+o < len(data[0]):
                        if s[i+o][j+o] == '#':
                            z += 1
                            break
                        elif s[i+o][j+o] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if i+o < len(data):
                        if s[i+o][j] == '#':
                            z += 1
                            break
                        elif s[i+o][j] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if i+o < len(data) and j-o >= 0:
                        if s[i+o][j-o] == '#':
                            z += 1
                            break
                        elif s[i+o][j-o] == 'L':
                            break
                    else:
                        break

                o = 0
                while True:
                    o += 1
                    if j-o >= 0:
                        if s[i][j-o] == '#':
                            z += 1
                            break
                        elif s[i][j-o] == 'L':
                            break
                    else:
                        break

                if z == 0:
                    n[i][j] = '#'
                elif z >= 5:
                    n[i][j] = 'L'

        if is_same(s, n):
            return count(n)
        else:
            s = n


print(solve())
