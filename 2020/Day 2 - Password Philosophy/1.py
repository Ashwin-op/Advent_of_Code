from collections import Counter

ans = 0
with open("input.txt") as fp:
    for line in fp.readlines():
        line = line.strip()

        contents = line.split(':')
        contents[1] = contents[1].strip()
        ch = contents[0][-1]
        range = contents[0].split()[0].split('-')

        c = Counter(contents[1])

        if int(range[0]) <= c[ch] and c[ch] <= int(range[1]):
            ans += 1

print(ans)
