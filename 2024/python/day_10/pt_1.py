map = []

zeroes = []

with open("input") as lines:
    for i, line in enumerate(lines):
        map.append([int(x) if x != "." else -1 for x in line.strip()])
        if 0 in map[-1]:
            for j in range(len(map[-1])):
                if map[-1][j] == 0:
                    zeroes.append((i, j))
            # zeroes.append((i, map[-1].index(0)))

# print(map)
print(zeroes)


def find_adjacent_increase(coords: tuple[int, int]):

    good = []
    nines_found = []
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        coord_to_check = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 > coord_to_check[0]) or (coord_to_check[0] >= len(map)):
            continue
        if (0 > coord_to_check[1]) or (coord_to_check[1] >= len(map[0])):
            continue

        if map[coord_to_check[0]][coord_to_check[1]] == map[coords[0]][coords[1]] + 1:
            good.append(coord_to_check)
            if map[coord_to_check[0]][coord_to_check[1]] == 9:
                nines_found.append(coord_to_check)

    return good, nines_found


nine_sum = 0
for zero_coords in zeroes:

    candidates = [zero_coords]
    nines_found = []
    while len(candidates) > 0:
        next = candidates.pop(0)
        more_candidates, new_nines = find_adjacent_increase(next)
        candidates += more_candidates
        nines_found += new_nines
    nines_found = list(set(nines_found))

    # print(f"Trailhead {zero_coords} found {len(nines_found)} nines: {nines_found}")
    nine_sum += len(nines_found)

print(f"Final Answer: {nine_sum}")
