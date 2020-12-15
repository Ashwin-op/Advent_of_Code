from collections import defaultdict


with open("input.txt") as fp:
    nums = [int(i) for i in fp.readline().strip().split(',')]

spoken = defaultdict(list)
turn = 1
last_number = None
while True:
    if turn <= len(nums):
        spoken_number = nums[turn - 1]
    else:
        if len(spoken[last_number]) == 1:
            spoken_number = 0
        else:
            spoken_number = spoken[last_number][-1] - spoken[last_number][-2]
    if turn == 30000000:
        print(spoken_number)
        break
    spoken[spoken_number].append(turn)
    last_number = spoken_number
    turn += 1
