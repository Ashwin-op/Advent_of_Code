with open("input.txt") as fp:
    instructions = [(line.strip('\n')[0], int(line.strip('\n')[1:]))
                    for line in fp]


moves = {'E': 1, 'W': -1, 'N': 1, 'S': -1, 'R': 1, 'L': -1}
sides = 'ESWN'
current_direction = 'E'
current_coords = (0, 0)

for instruction in instructions:
    if instruction[0] == 'F':
        instruction = (current_direction, instruction[1])

    if instruction[0] in 'EW':
        current_coords = (
            current_coords[0] + instruction[1] * moves[instruction[0]], current_coords[1])
    elif instruction[0] in 'NS':
        current_coords = (
            current_coords[0], current_coords[1] + instruction[1] * moves[instruction[0]])

    if instruction[0] in 'RL':
        rotation = int((instruction[1] / 90) % 4)
        new_index = (sides.index(current_direction) +
                     rotation * moves[instruction[0]]) % 4
        current_direction = sides[new_index]

print(abs(current_coords[0]) + abs(current_coords[1]))
