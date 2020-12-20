def lmap(func, x): return list(map(func, x))


def rotate(tile, num, size=10):
    newt = [[tile[i][j] for j in range(size)] for i in range(size)]
    for _ in range(num):
        newt = [[newt[j][size-1-i] for j in range(size)] for i in range(size)]
    return newt


def flip(tile, size=10):
    return [[tile[i][size-1-j] for j in range(size)] for i in range(size)]


def place(tile, image, pos, size=10):
    for i in range(size):
        for j in range(size):
            image[pos[0]*size+i][pos[1]*size+j] = tile[i][j]


with open("input.txt") as fp:
    data = fp.read().strip().split("\n")

sides = {}
tiles = {}
for i in range(0, len(data), 12):
    id = int(data[i][5:-1])
    tiles[id] = data[i+1:i+11]
    u, l, r, d = "", "", "", ""
    for j in range(10):
        bu, bl, br, bd = [data[i+1][j], data[i-j+10][0],
                          data[i+j+1][9], data[i+10][9-j]]
        u, l, r, d = lmap(
            lambda x: x[0]+x[1],
            zip([u, l, r, d], [bu, bl, br, bd])
        )
    sides[id] = [u, r, d, l]

corners = []
edges = []
internal = []
side_match = {}
for id1 in sides:
    outsides = 0
    side_match[id1] = [(-1, False), (-1, False), (-1, False), (-1, False)]
    for i1, side in enumerate(sides[id1]):
        found = False
        for id2 in sides:
            if id1 == id2:
                continue
            for i2, side2 in enumerate(sides[id2]):
                s2 = side2[::-1]
                if side == s2 or side == side2:
                    side_match[id1][i1] = (id2, i2)
                    found = True
                    break
            if found:
                break
        if not found:
            outsides += 1
    if outsides == 2:
        corners.append(id1)

image = [['.' for i in range(120)] for j in range(120)]
img_tile = [[[0, 0] for j in range(12)] for i in range(12)]
init_rot, num = 2, 12  # input data
ul_corner = rotate(tiles[corners[0]], init_rot)
for i in range(num):
    for j in range(num):
        flipped = False
        tile_rot = 0
        if (i, j) == (0, 0):
            img_tile[0][0] = [corners[0], init_rot]
            tile_rot = init_rot
            place(ul_corner, image, (i, j))
        else:
            tile_id, _ = img_tile[i][j]
            found = False
            for r in range(4):
                rot = rotate(tiles[tile_id], r)
                if j == 0:
                    pr_side = [image[10*i-1][10*j+k] for k in range(10)]
                    side = rot[0]
                else:
                    pr_side = [image[10*i+k][10*j-1] for k in range(10)]
                    side = [rot[k][0] for k in range(10)]
                if side == pr_side:
                    found = True
                    place(rot, image, (i, j))
                    tile_rot = r
                    break
            if not found:
                tile = flip(tiles[tile_id])
                flipped = True
                for r in range(4):
                    rot = rotate(tile, r)
                    if j == 0:
                        pr_side = [image[10*i-1][10*j+k] for k in range(10)]
                        side = rot[0]
                    else:
                        pr_side = [image[10*i+k][10*j-1] for k in range(10)]
                        side = [rot[k][0] for k in range(10)]
                    if side == pr_side:
                        found = True
                        place(rot, image, (i, j))
                        tile_rot = r
                        break
            if not found:
                print("NOT FOUND")
                for row in tiles[tile_id]:
                    print(''.join(row))
                break
        if j != num-1:
            sides = side_match[img_tile[i][j][0]]
            s = sides
            if flipped:
                s = [sides[0], sides[3], sides[2], sides[1]]
            next_id = s[(tile_rot+1) % 4][0]
            img_tile[i][j+1][0] = next_id
        if j == 0 and i != num-1:
            sides = side_match[img_tile[i][0][0]]
            s = sides
            if flipped:
                s = [sides[0], sides[3], sides[2], sides[1]]
            next_id = s[(tile_rot+2) % 4][0]
            img_tile[i+1][j][0] = next_id

final_image = [[' ' for j in range(num*8)] for i in range(num*8)]
for i in range(num):
    for j in range(num):
        for r in range(8):
            for c in range(8):
                final_image[i*8+r][j*8+c] = image[i*10+r+1][j*10+c+1]

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
mlen = len(monster[0])
orig_hash = sum([row.count('#') for row in final_image])

img_flipped = flip(final_image, len(final_image))
for rot in range(4):
    imag = rotate(final_image, rot, len(final_image))
    imag_flip = rotate(img_flipped, rot, len(final_image))
    for i in range(len(final_image)-len(monster)):
        for j in range(len(final_image[0])-mlen):
            match = True
            for mr in range(3):
                for mc in range(mlen):
                    if monster[mr][mc] == '#':
                        if imag[i+mr][j+mc] == '.':
                            match = False
                            break
                if not match:
                    break
            if match:
                for mr in range(3):
                    for mc in range(mlen):
                        if monster[mr][mc] == '#':
                            imag[i+mr][j+mc] = 'O'
    ans = sum([row.count('#') for row in imag])
    if ans != orig_hash:
        print(ans)
    for i in range(len(final_image)-len(monster)):
        for j in range(len(final_image[0])-mlen):
            match = True
            for mr in range(3):
                for mc in range(mlen):
                    if monster[mr][mc] == '#':
                        if imag_flip[i+mr][j+mc] == '.':
                            match = False
                            break
                if not match:
                    break
            if match:
                for mr in range(3):
                    for mc in range(mlen):
                        if monster[mr][mc] == '#':
                            imag_flip[i+mr][j+mc] = 'O'
    ans = sum([row.count('#') for row in imag_flip])
    if ans != orig_hash:
        print(ans)
