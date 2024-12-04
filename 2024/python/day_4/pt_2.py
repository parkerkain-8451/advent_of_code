input = []
with open("input") as lines:
    for line in lines:
        input.append(line.replace("\n", ""))

# print(input)

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


# Look for A's, then look for the others
for i in range(1, len(input) - 1):
    for j in range(1, len(input[0]) - 1):
        if input[i][j] == "A":
            print(f"A Found at {i}, {j}!")
            mas_count = 0
            if input[i - 1][j - 1] == "M" and input[i + 1][j + 1] == "S":
                mas_count += 1
            elif input[i - 1][j - 1] == "S" and input[i + 1][j + 1] == "M":
                mas_count += 1

            if input[i - 1][j + 1] == "M" and input[i + 1][j - 1] == "S":
                mas_count += 1
            elif input[i - 1][j + 1] == "S" and input[i + 1][j - 1] == "M":
                mas_count += 1

            if mas_count == 2:
                times_found += 1
            elif mas_count > 2:
                raise ValueError
            else:
                continue


print(f"Times Found: {times_found}")
