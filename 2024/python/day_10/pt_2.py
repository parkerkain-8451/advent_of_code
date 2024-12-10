import numpy as np

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


def find_adjacent_increase(path: list[tuple[int, int]]):

    good = []
    nines_found = []
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        coord_to_check = (path[-1][0] + direction[0], path[-1][1] + direction[1])
        if (0 > coord_to_check[0]) or (coord_to_check[0] >= len(map)):
            continue
        if (0 > coord_to_check[1]) or (coord_to_check[1] >= len(map[0])):
            continue

        if (
            map[coord_to_check[0]][coord_to_check[1]]
            == map[path[-1][0]][path[-1][1]] + 1
        ):
            new_path = path.copy()
            new_path.append(coord_to_check)
            good.append(new_path)
            if map[coord_to_check[0]][coord_to_check[1]] == 9:
                nines_found.append(new_path)

    return good, nines_found


path_sum = 0
for zero_coords in zeroes:

    candidates = [[zero_coords]]
    paths_found = []
    while len(candidates) > 0:
        next = candidates.pop(0)
        more_candidates, new_nines = find_adjacent_increase(next)
        candidates += more_candidates
        paths_found += new_nines
    # paths_found = list(set(paths_found))
    paths_found = np.unique(np.array(paths_found), axis=0)

    # print(f"Trailhead {zero_coords} found {len(paths_found)} paths: {paths_found}")
    path_sum += len(paths_found)
print(f"Final Answer: {path_sum}")
