def check_sum(nums, k):
    s = set()

    for i in range(0, len(nums)):
        temp = k-nums[i]
        if (temp in s):
            return True
        s.add(nums[i])
    return False


with open("input.txt") as fp:
    nums = [int(i) for i in fp.read().split('\n')[:-1]]

for i in range(25, len(nums)):
    if not check_sum(nums[i-25:i], nums[i]):
        print(nums[i])
        break
