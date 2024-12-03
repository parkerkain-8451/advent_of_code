import math

left_list = []
right_list = []

with open("input") as file:
    for line in file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

left_list = sorted(left_list)
right_list = sorted(right_list)

total = 0
for l, r in zip(left_list, right_list):
    total += abs(l - r)

print(f"Final Total: {total}")
