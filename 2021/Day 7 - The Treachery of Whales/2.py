from statistics import mean

with open("input.txt") as f:
    values = [int(i) for i in f.readline().split(",")]

m_values = int(mean(values))

print(min(
    sum(sum(range(1, abs(pos - i) + 1)) for pos in values)
    for i in range(m_values - 1, m_values + 1)
))
