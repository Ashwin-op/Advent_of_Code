with open("input.txt") as fp:
    answers = [i.split('\n') for i in fp.read().split('\n\n')]
answers[-1].pop()

sumCounts = sum([len(set.intersection(*map(set, i))) for i in answers])
print(sumCounts)
