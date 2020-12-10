from collections import Counter


with open("input.txt") as fp:
    adapters = sorted([int(i.strip()) for i in fp.readlines()])
    adapters = [0] + adapters + [adapters[-1] + 3]


dp = [0] * (adapters[-1] + 1)
dp[0] = 1

for a in adapters:
    for j in range(1, 4):
        prev = a - j
        dp[a] += dp[prev] if prev >= 0 else 0

print(dp[-1])
