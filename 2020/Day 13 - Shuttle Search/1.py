with open("input.txt") as fp:
    startTime = int(fp.readline().strip())
    busTimes = [int(i) for i in fp.readline().split(',') if i != 'x']


def closestMultiple(n, x):
    if x > n:
        return x
    z = int(x / 2)
    n = n + z
    n = n - (n % x)
    return n


multiples = [closestMultiple(startTime, i) for i in busTimes]
busToTake = min(i for i in multiples if i >= startTime)

print((busToTake-startTime)*(busTimes[multiples.index(busToTake)]))
