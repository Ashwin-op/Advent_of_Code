with open("input.txt") as fp:
    instructions = [i.split() for i in fp.read().split('\n')][:-1]

accumulator = 0
instDone = []

i = 0
while True:
    if i in instDone:
        break
    instDone.append(i)
    if instructions[i][0] == "acc":
        accumulator += int(instructions[i][1])
        i += 1
    elif instructions[i][0] == "jmp":
        i += int(instructions[i][1])
    elif instructions[i][0] == "nop":
        i += 1

print(accumulator)
