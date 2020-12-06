with open("input.txt") as fp:
    answers = [i.replace('\n', '') for i in fp.read().split('\n\n')]

sumCounts = sum([len(set(i)) for i in answers])
print(sumCounts)
