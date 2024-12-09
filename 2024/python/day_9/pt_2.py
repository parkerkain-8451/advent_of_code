with open("input") as lines:
    for line in lines:
        input = line.strip()

print(input)

files = []

for i, curr in enumerate(input):
    if i % 2 == 0:
        files.append((i // 2, int(curr)))
    else:
        files.append((-1, int(curr)))

print(files)

print("Beginning")
for i in range(len(files) - 1, -1, -1):
    # print(files)
    # print("============================")
    if files[i][0] == -1:
        continue

    for j in range(0, i):
        if files[j][0] != -1:
            continue

        if files[j][1] < files[i][1]:
            continue
        elif files[j][1] == files[i][1]:
            files[j] = files[i]
            files[i] = (-1, files[i][1])
            # print(f"A Perfect Fit!")
            break
        else:
            # print(f"An imperfect fit!")
            leftover_space = files[j][1] - files[i][1]
            files[j] = (files[j][0], leftover_space)
            tmp = files[i]
            # print((-1, files[i][1]), "!!!", i)
            files[i] = (-1, files[i][1])
            # print(f"Inserting {tmp} at {i}")
            files.insert(j, tmp)
            break

    cap = len(files)
    change_made = True
    for j in range(1, cap):
        if files[j][1] == 0:
            # Remove the file
            # print(f"Removing {files[j]}")
            files.pop(j)
            cap -= 1
            j -= 1
            change_made = True
        elif files[j][0] == -1 and files[j - 1][0] == -1:
            # print(f"Combining {j, files[j]} and {j-1, files[j - 1]}")
            files[j - 1] = (-1, files[j][1] + files[j - 1][1])
            files.pop(j)
            j -= 1
            change_made = True

        if change_made:
            break

        # print("Nothin to combine or remove")

print(files)
total = 0
i = 0
for curr in files:
    # print(curr)
    if curr[0] == -1:
        i += curr[1]
        continue

    times = curr[1]
    while times > 0:
        # print(f"{i} * {curr[0]}")
        total += i * curr[0]
        times -= 1
        i += 1

print(total)


# next_file = 0
# adjusted_files = []
# filled_gaps = []
# order = []
# # Fill the gaps
# for gap in gaps:
#     adjusted_files.append(files[next_file])
#     files[next_file] = (files[next_file][0], 0)
#     order.append(0)
#     next_file += 1
#
#     gap_filled = False
#     for i in range(len(files) - 1, -1, -1):
#         curr_file = files[i]
#         if curr_file[1] == 0:
#             continue
#
#         if curr_file[1] <= gap:
#             # print(f"Pushing {curr_file}!")
#             filled_gaps.append(curr_file)
#             order.append(1)
#             files[i] = (files[i][0], 0)
#             gap -= curr_file[1]
#             if gap == 0:
#                 gap_filled = True
#                 break
#
#     if gap_filled == False:
#         filled_gaps.append((0, gap))
#         order.append(1)
#
#
# print("==========================")
# print(adjusted_files)
# print(filled_gaps)
# print(order)
# print("==========================")

# big = []
# files_i = 0
# gaps_i = 0
# for i in order:
#     # print(f"{i=}")
#     if i == 1:
#         big += [filled_gaps[gaps_i][0]] * filled_gaps[gaps_i][1]
#         # print(f"{gaps_i=}")
#         gaps_i += 1
#     else:
#         big += [adjusted_files[files_i][0]] * adjusted_files[files_i][1]
#         # print(f"{files_i=}")
#         files_i += 1
#
# print(big)
# total = 0
# for i, curr in enumerate(big):
#     total += i * curr
#
# print(f"{total=}")


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
