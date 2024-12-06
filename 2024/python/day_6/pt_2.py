import numpy as np

input = []

with open("input") as lines:
    for i, line in enumerate(lines):
        input.append(list(line.replace("\n", "")))
        if "v" in list(line):
            starting_coord = (i, list(line).index("v"))
            starting_direction = "down"
        elif "<" in list(line):
            starting_coord = (i, list(line).index("<"))
            starting_direction = "left"
        if ">" in list(line):
            starting_coord = (i, list(line).index(">"))
            starting_direction = "right"
        if "^" in list(line):
            starting_coord = (i, list(line).index("^"))
            starting_direction = "up"

input = np.array(input)


def find_next_object(coord: tuple[int, int], direction: str, input):
    if direction == "up":
        slice = input[0 : coord[0], coord[1]]
        next_direction = "right"
    elif direction == "down":
        slice = input[coord[0] + 1 : len(input), coord[1]]
        next_direction = "left"
    elif direction == "left":
        slice = input[coord[0], 0 : coord[1]]
        next_direction = "up"
    elif direction == "right":
        slice = input[coord[0], coord[1] + 1 : len(input[coord[0]])]
        next_direction = "down"
    else:
        raise ValueError

    if ("#" in slice) and (direction in ["up", "left"]):
        next_wall = len(slice) - 1 - list(slice)[::-1].index("#")
    elif "#" in slice:
        next_wall = list(slice).index("#")
    # print(slice, next_wall)

    if direction == "up":
        if "#" not in slice:
            new_coord = (0, coord[1])
            next_direction = "done"
        else:
            new_coord = (next_wall + 1, coord[1])
        painted = [(x, coord[1]) for x in range(new_coord[0], coord[0])]
    elif direction == "down":
        if "#" not in slice:
            new_coord = (len(input) - 1, coord[1])
            next_direction = "done"
        else:
            new_coord = (coord[0] + next_wall, coord[1])
        painted = [(x, coord[1]) for x in range(coord[0] + 1, new_coord[0] + 1)]
    elif direction == "left":
        if "#" not in slice:
            new_coord = (coord[0], 0)
            next_direction = "done"
        else:
            new_coord = (coord[0], next_wall + 1)
        painted = [(coord[0], x) for x in range(new_coord[1], coord[1])]
    elif direction == "right":
        if "#" not in slice:
            new_coord = (coord[0], len(input[coord[1]]))
            next_direction = "done"
        else:
            new_coord = (coord[0], coord[1] + next_wall)
        painted = [(coord[0], x) for x in range(coord[1] + 1, new_coord[1] + 1)]

    # Return all of the painted indicies, the new coord of the guard, and their new direction
    return painted, new_coord, next_direction


loops = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        input_copy = input.copy()
        input_copy[i, j] = "#"
        # print(i, j)
        # print(input_copy)
        painted = [(starting_coord)]
        coord = starting_coord
        direction = starting_direction
        coord_dir_combos = [(starting_coord, starting_direction)]
        while direction != "done":
            # print(coord, direction, painted)
            new_painted, new_coord, new_direction = find_next_object(
                coord=coord, direction=direction, input=input_copy
            )
            direction = new_direction
            coord = new_coord
            painted += new_painted
            if (coord, direction) in coord_dir_combos:
                print("loop found!")
                loops += 1
                break
            coord_dir_combos.append((coord, direction))
print(loops)
