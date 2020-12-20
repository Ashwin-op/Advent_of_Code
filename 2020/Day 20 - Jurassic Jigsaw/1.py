def lmap(func, x): return list(map(func, x))


with open("input.txt") as fp:
    data = fp.read().strip().split("\n")


sides = {}
tiles = {}
for i in range(0, len(data), 12):
    id = int(data[i][5:-1])
    tiles[id] = data[i+1:i+10]
    u, l, r, d = "", "", "", ""
    for j in range(10):
        bu, bl, br, bd = [data[i+1][j], data[i-j+10][0],
                          data[i+j+1][9], data[i+10][9-j]]
        u, l, r, d = lmap(
            lambda x: x[0]+x[1],
            zip([u, l, r, d], [bu, bl, br, bd])
        )
    sides[id] = [u, r, d, l]

res = 1
corners = []
edges = []
internal = []
for id1 in sides:
    outsides = 0
    for side in sides[id1]:
        found = False
        for id2 in sides:
            if id1 == id2:
                continue
            for side2 in sides[id2]:
                s2 = side2[::-1]
                if side == s2 or side == side2:
                    found = True
                    break
            if found:
                break
        if not found:
            outsides += 1
    if outsides == 2:
        res *= id1
print(res)
