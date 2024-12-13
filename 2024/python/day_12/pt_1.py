input = []

with open("input_smol_2") as lines:
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

total = 0
for k in regions:
    for curr in regions[k]:
        print(
            f"A region of {k} plans with price {curr['area']} * {curr['perimeter']} = {curr['area'] * curr['perimeter']}"
        )
        total += curr["area"] * curr["perimeter"]

print(f"Final Answer: {total}")
