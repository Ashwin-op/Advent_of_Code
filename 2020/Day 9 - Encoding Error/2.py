def check_sum(nums, k):
    s = set()

    for i in range(0, len(nums)):
        temp = k-nums[i]
        if (temp in s):
            return True
        s.add(nums[i])
    return False


def subArraySum(nums, sum):
    curr_sum = nums[0]
    start = 0

    i = 1
    while i <= len(nums):
        while curr_sum > sum and start < i-1:
            curr_sum = curr_sum - nums[start]
            start += 1

        if curr_sum == sum:
            return start, i - 1

        if i < len(nums):
            curr_sum = curr_sum + nums[i]
        i += 1

    return 0, 0


with open("input.txt") as fp:
    nums = [int(i) for i in fp.read().split('\n')[:-1]]

for i in range(25, len(nums)):
    if not check_sum(nums[i-25:i], nums[i]):
        start, end = subArraySum(nums, nums[i])
        range = nums[start:end+1]
        print(min(range) + max(range))
        break
