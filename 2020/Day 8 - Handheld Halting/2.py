def solve(instructions):
    accumulator = 0
    curr_instruction = 0
    visited_instructions = set()

    while curr_instruction not in visited_instructions:
        if curr_instruction >= len(instructions):
            return True, accumulator

        visited_instructions.add(curr_instruction)

        operation, argument = instructions[curr_instruction]
        if operation == 'jmp':
            curr_instruction += argument
            continue

        if operation == 'acc':
            accumulator += argument
        curr_instruction += 1

    return False, accumulator


def parse(line):
    operation, argument = line.split()
    return (operation, int(argument[1:]) if argument[0] == '+' else -1 * int(argument[1:]))


with open("input.txt") as fp:
    instructions = [parse(line) for line in fp.read().split('\n') if line != '']
for i, (operation, argument) in enumerate(instructions):
    if operation == 'acc':
        continue

    modified_instructions = list(instructions)
    if operation == 'jmp':
        modified_instructions[i] = ('nop', argument)
    else:
        modified_instructions[i] = ('jmp', argument)
    terminated, accumulator = solve(modified_instructions)

    if terminated:
        print(accumulator)
        break
