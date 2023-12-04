import re

f = open("input", "r")
lines = f.readlines()

# lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
# ]
lines = [x.split(": ")[1].replace("\n", "").strip() for x in lines]
print(lines)

points = []
for curr_line in lines:
    winning_raw, nums_raw = curr_line.split("|")
    winning = set(re.split(" +", winning_raw)[:-1])
    nums = re.split(" +", nums_raw)[1:]
    print(winning, nums)

    curr_power = 0
    for num in nums:
        if num in winning:
            curr_power += 1

    if curr_power != 0:
        points.append(2 ** (curr_power - 1))

print(points)
print(f"Part 1 Answer: {sum(points)}")
