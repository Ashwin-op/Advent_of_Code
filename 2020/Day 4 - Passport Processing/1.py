passports = []
with open("input.txt") as fp:
    data = []
    for i in fp.readlines():
        if i != "\n":
            data.append(i.strip().split())
        else:
            passports.append(data)
            data = []

passports = [sum(i, []) for i in passports]

ans = 0
for i in passports:
    present = []
    for fields in i:
        present.append(fields.split(':')[0])
    if len(present) == 8 or (len(present) == 7 and 'cid' not in present):
        ans += 1

print(ans)
