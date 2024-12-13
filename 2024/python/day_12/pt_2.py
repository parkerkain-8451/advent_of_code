input = []

with open("input") as lines:
    for line in lines:
        input.append(list(line.replace("\n", "")))

print(input)

visited_plots = []
regions = {}


def blobify(coord: tuple[int, int], region):
    if coord in visited_plots:
        return region
    curr_letter = input[coord[0]][coord[1]]
    region["area"] += 1
    region["plots"].append(coord)
    visited_plots.append(coord)
    to_visit = []

    # print(f"Looking around {coord}")
    for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_coord = (coord[0] + direction[0], coord[1] + direction[1])
        if (
            (new_coord[0] < 0)
            or (new_coord[0] >= len(input))
            or (new_coord[1] < 0)
            or (new_coord[1] >= len(input[0]))
        ):
            # print(f"{new_coord} is out of bounds")
            region["perimeter"] += 1
        elif (input[new_coord[0]][new_coord[1]] == curr_letter) and (
            new_coord in visited_plots
        ):
            # print(f"{new_coord} has been visited before")
            continue
        elif (input[new_coord[0]][new_coord[1]] == curr_letter) and (
            new_coord not in visited_plots
        ):
            # print(f"{new_coord} is good!")
            to_visit.append(new_coord)
        else:
            # print(f"{new_coord} is a different type!")
            region["perimeter"] += 1

    # print(region)
    for next in to_visit:
        region = blobify(coord=next, region=region)

    return region


for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        if (i, j) not in visited_plots:
            # print("new plot just dropped ", i, j)
            region = {"perimeter": 0, "plots": [], "area": 0}
            region = blobify(coord=(i, j), region=region)
            if input[i][j] not in regions:
                regions[input[i][j]] = [region]
            else:
                regions[input[i][j]].append(region)
            # print(region)
print(regions)


def is_out(coords, region_letter):
    if (
        coords[0] < 0
        or coords[0] >= len(input)
        or coords[1] < 0
        or coords[1] >= len(input[0])
    ):
        return True

    if input[coords[0]][coords[1]] != region_letter:
        return True

    return False


total = 0
for k in regions:
    # for k in ["C"]:
    for curr in regions[k]:
        print("==================")
        print(curr)
        sides = 0
        region_min_0 = min([x[0] for x in curr["plots"]])
        region_min_1 = min([x[1] for x in curr["plots"]])
        region_max_0 = max([x[0] for x in curr["plots"]])
        region_max_1 = max([x[1] for x in curr["plots"]])
        for i in range(region_min_0, region_max_0 + 1):
            for j in range(region_min_1, region_max_1 + 1):
                curr_sides = 0
                if input[i][j] != k:
                    continue
                if (
                    is_out((i + 1, j), k)
                    and is_out((i - 1, j), k)
                    and is_out((i, j + 1), k)
                    and is_out((i, j - 1), k)
                    and (i, j) != curr["plots"][0]
                ):
                    continue

                if (i, j) not in curr["plots"]:
                    continue
                # print(i, j)

                for delta_1, delta_2 in [
                    ((0, 1), (1, 0)),
                    ((0, 1), (-1, 0)),
                    ((0, -1), (1, 0)),
                    ((0, -1), (-1, 0)),
                ]:
                    # print(delta_1, delta_2)
                    # print((i, j + delta_1[1]), (i + delta_2[0], j))
                    # exit()
                    if is_out((i, j + delta_1[1]), k) and is_out(
                        (i + delta_2[0], j), k
                    ):
                        # print(f"Adjacent sides are out - corner!")
                        curr_sides += 1

                for diag in [
                    (1, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                ]:
                    diag_coord = i + diag[0], j + diag[1]
                    diag_out = is_out(diag_coord, k)
                    abut_1_coord = i, j + diag[1]
                    abut_1_out = is_out(abut_1_coord, k)
                    abut_2_coord = i + diag[0], j
                    abut_2_out = is_out(abut_2_coord, k)

                    if not diag_out and sum([abut_1_out, abut_2_out]) == 1:
                        # print(f"we got a live one!")
                        curr_sides += 0.5
                print(f"Spot {i, j} contribution: {curr_sides}")
                sides += curr_sides
        print(f"Total sides for region {k}: {sides}")
        total += sides * curr["area"]

        # print(
        #     f"A region of {k} plans with price {curr['area']} * {curr['perimeter']} = {curr['area'] * curr['perimeter']}"
        # )
        # total += curr["area"] * curr["perimeter"]

print(f"Final Answer: {total}")
