input = []
with open("input") as lines:
    for line in lines:
        input.append(line.replace("\n", ""))

times_found = 0

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
