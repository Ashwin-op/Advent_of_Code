from statistics import median


with open("input.txt") as f:
    values = [int(i) for i in f.readline().split(",")]

print(sum(abs(i - median(values)) for i in values))
