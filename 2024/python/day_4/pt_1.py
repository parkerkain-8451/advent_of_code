input = []
with open("input") as lines:
    for line in lines:
        input.append(line.replace("\n", ""))

print(input)

times_found = 0


def search_adjacent(center: tuple[int, int], needle: str):
    matches = []
    for x_delta in [-1, 0, 1]:
        for y_delta in [-1, 0, 1]:
            if (0 > center[0] + 3 * x_delta) or (center[0] + 3 * x_delta >= len(input)):
                print("Skipping...")
                continue
            if (0 > center[1] + 3 * y_delta) or (center[1] + 3 * y_delta >= len(input)):
                print("Skipping...")
                continue
            print(center[0] + x_delta, center[1] + y_delta)
            curr = center[0] + x_delta, center[1] + y_delta
            if input[curr[0]][curr[1]] == needle:
                print(f"Adjacent {needle} found at {curr}")
                matches.append((curr, (x_delta, y_delta)))

    return matches


# Look for X's, then search adjacent for M, then adjacent in the SAME DIRECTION for A and S
for i in range(len(input)):
    for j in range(len(input[0])):
        # print(i, j)
        if input[i][j] == "X":
            print(f"X Found at {i}, {j}!")
            matched_m = search_adjacent(center=(i, j), needle="M")
            for curr_match, curr_delta in matched_m:
                # print(curr_delta)
                if input[i + 2 * curr_delta[0]][j + 2 * curr_delta[1]] == "A":
                    print("We got an A!")
                    if input[i + 3 * curr_delta[0]][j + 3 * curr_delta[1]] == "S":
                        print("We got an S!")
                        times_found += 1

print(f"Times Found: {times_found}")
