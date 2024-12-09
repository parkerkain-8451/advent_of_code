import re

input = []
coords = {}

with open("input") as lines:
    for i, line in enumerate(lines):
        input.append(line.replace("\n", ""))
        # print(line, len(line))
        specials = re.findall(r"[0-9]|[a-z]|[A-Z]", line)
        # print(specials)
        for j, curr in enumerate(line):
            if curr in specials:
                if curr in coords:
                    coords[curr].append((i, j))
                else:
                    coords[curr] = [(i, j)]

candidates = []
for curr_symbol in coords:
    for i, curr_coord_1 in enumerate(coords[curr_symbol]):
        for j, curr_coord_2 in enumerate(coords[curr_symbol][i + 1 :]):
            delta_x = curr_coord_2[0] - curr_coord_1[0]
            delta_y = curr_coord_2[1] - curr_coord_1[1]
            # print(curr_coord_1, curr_coord_2, (delta_x, delta_y))

            candidate_1 = curr_coord_1[0] - delta_x, curr_coord_1[1] - delta_y
            candidate_2 = curr_coord_2[0] + delta_x, curr_coord_2[1] + delta_y

            # print(candidate_1, candidate_2)
            candidates.append(candidate_1)
            candidates.append(candidate_2)

good = []
print(len(input), len(input[1]))
for curr in candidates:
    if (
        curr[0] >= 0
        and curr[0] < len(input)
        and curr[1] >= 0
        and curr[1] < len(input[0])
    ):
        good.append(curr)

good = list(set(good))
print(len(good))
