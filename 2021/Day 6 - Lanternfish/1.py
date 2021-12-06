with open("input.txt") as f:
    values = [int(i) for i in f.readline().split(",")]


fish = {i: 0 for i in range(-1, 9)}

for val in values:
    fish[val] += 1

for i in range(80):
    for j in range(len(fish) - 1):
        fish[j - 1] = fish[j]

    fish[8] = fish[-1]
    fish[6] += fish[-1]
    fish[-1] = 0

print(sum(list(fish.values())))
