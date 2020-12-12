with open("input.txt") as fp:
    instructions = [(line.strip('\n')[0], int(line.strip('\n')[1:]))
                    for line in fp]

moves = {'E': 1, 'W': -1, 'N': 1, 'S': -1, 'R': 1, 'L': -1}
sides = 'ESWN'
current_direction = 'E'
current_coords = (0, 0)
current_waypoint_offset = (10, 1)
current_waypoint_coords = (
    current_coords[0] + current_waypoint_offset[0], current_coords[1] + current_waypoint_offset[1])

for instruction in instructions:
    if instruction[0] == 'F':
        temp = instruction[1]
        current_coords = (current_coords[0] + current_waypoint_offset[0]
                          * temp, current_coords[1] + current_waypoint_offset[1] * temp)

    if instruction[0] in 'EW':
        current_waypoint_offset = (
            current_waypoint_offset[0] + instruction[1] * moves[instruction[0]], current_waypoint_offset[1])
    elif instruction[0] in 'NS':
        current_waypoint_offset = (
            current_waypoint_offset[0], current_waypoint_offset[1] + instruction[1] * moves[instruction[0]])

    if instruction[0] in 'RL':
        rotations = [
            current_waypoint_offset,
            (current_waypoint_offset[1], - current_waypoint_offset[0]),
            (- current_waypoint_offset[0], - current_waypoint_offset[1]),
            (- current_waypoint_offset[1], current_waypoint_offset[0]),
        ]

        rotation = int((instruction[1] / 90) % 4)
        new_index = (sides.index(current_direction) +
                     rotation * moves[instruction[0]]) % 4
        current_waypoint_offset = rotations[new_index]

    current_waypoint_coords = (
        current_coords[0] + current_waypoint_offset[0], current_coords[1] + current_waypoint_offset[1])

print(abs(current_coords[0]) + abs(current_coords[1]))
