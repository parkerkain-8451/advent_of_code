with open("input") as lines:
    for line in lines:
        input = line.strip()

print(input)

files = []
gaps = []

for i, curr in enumerate(input):
    if i % 2 == 0:
        files.append((i // 2, int(curr)))
    else:
        gaps.append(int(curr))

print(files)
print(gaps)

next_file = 0
adjusted_files = []
filled_gaps = []
order = []
# Fill the gaps
for gap in gaps:
    # print(f"Pushing {files[next_file]}")
    adjusted_files.append(files[next_file])
    files[next_file] = (files[next_file][0], 0)
    order.append(0)
    next_file += 1

    if gap == 0:
        continue

    gap_filled = False
    for i in range(len(files) - 1, -1, -1):
        curr_file = files[i]
        if curr_file[1] == 0:
            continue

        if curr_file[1] <= gap:
            # print(f"Pushing {curr_file}!")
            filled_gaps.append(curr_file)
            order.append(1)
            files[i] = (files[i][0], 0)
            gap -= curr_file[1]
        else:
            # print(f"Pushing {curr_file[0], gap}!!")
            filled_gaps.append((curr_file[0], gap))
            files[i] = (files[i][0], files[i][1] - gap)
            gap = 0
            order.append(1)

        if gap == 0:
            break


print("==========================")
print(adjusted_files)
print(filled_gaps)
print(order)
print("==========================")

big = []
files_i = 0
gaps_i = 0
for i in order:
    # print(f"{i=}")
    if i == 1:
        big += [filled_gaps[gaps_i][0]] * filled_gaps[gaps_i][1]
        # print(f"{gaps_i=}")
        gaps_i += 1
    else:
        big += [adjusted_files[files_i][0]] * adjusted_files[files_i][1]
        # print(f"{files_i=}")
        files_i += 1

print(big)
total = 0
for i, curr in enumerate(big):
    total += i * curr

print(f"{total=}")


# files_i = 0
# gaps_i = 0
# big = ""
# for i in order:
#     if i == 0:
#         big += str(adjusted_files[files_i][0]) * adjusted_files[files_i][1]
#         files_i += 1
#     else:
#         big += str(filled_gaps[gaps_i][0]) * filled_gaps[gaps_i][1]
#         gaps_i += 1

# print(big)

# total = 0
# for i, curr in enumerate(big):
#     total += i * int(curr)
#
# print(f"Final Answer: {total}")
