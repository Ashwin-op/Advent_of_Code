import math


with open("1.txt") as fp:
    numbers = [int(i.strip()) for i in fp.readlines()]


def threeSum(arr, sum):
    arr.sort()
    for i in range(len(arr) - 2):
        l = i + 1
        r = len(arr)-1
        while (l < r):
            if(arr[i] + arr[l] + arr[r] == sum):
                return [arr[i], arr[l], arr[r]]
            elif (arr[i] + arr[l] + arr[r] < sum):
                l += 1
            else:
                r -= 1


print(math.prod(threeSum(numbers, 2020)))
