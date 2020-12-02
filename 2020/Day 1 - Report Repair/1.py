import math


with open("1.txt") as fp:
    numbers = [int(i.strip()) for i in fp.readlines()]


def twoSum(arr, sum):
    s = set()

    for i in range(len(arr)):
        temp = sum - arr[i]
        if temp in s:
            return [arr[i], temp]
        s.add(arr[i])


print(math.prod(twoSum(numbers, 2020)))
