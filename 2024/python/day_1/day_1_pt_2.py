from collections import Counter

left_list = []
right_list = []

with open("input") as file:
    for line in file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

lookup = Counter(right_list)

total = 0
for curr in left_list:
    total += curr * lookup[curr]


print(f"Final Total: {total}")
