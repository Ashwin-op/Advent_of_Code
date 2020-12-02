ans = 0
with open("input.txt") as fp:
    for line in fp.readlines():
        line = line.strip()

        contents = line.split(':')
        contents[1] = contents[1].strip()
        ch = contents[0][-1]
        pos = contents[0].split()[0].split('-')

        if bool(contents[1][int(pos[0]) - 1] == ch) ^ bool(contents[1][int(pos[1]) - 1] == ch):
            ans += 1

print(ans)
