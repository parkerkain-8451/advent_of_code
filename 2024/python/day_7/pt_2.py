import re
import itertools as it
import more_itertools as mit


input = []
with open("input") as lines:
    for line in lines:
        parts = re.split(r": | ", line)
        input.append([int(parts[0]), [int(x) for x in parts[1:]]])


# print(input)


def find_triplets(target):
    triplets = []
    for i in range(target + 1):
        for j in range(target + 1 - i):
            for k in range(target + 1 - i - j):
                if i + j + k == target:
                    triplets.append((i, j, k))
    return triplets


good_ones = []
for value, numbers in input:
    # print(value, numbers)
    adds_up = False

    operators = ["+", "*", "||"]
    all_perms = []
    triples = find_triplets(len(numbers))
    for plusses, multipliers, parens in triples:
        all_perms += mit.distinct_permutations(
            (["+"] * plusses) + (["*"] * multipliers) + (["||"] * parens)
        )

    for curr_perm in all_perms:
        result = numbers[0]
        for curr_number, curr_operand in zip(numbers[1:], curr_perm):
            if curr_operand == "+":
                result += curr_number
            elif curr_operand == "*":
                result *= curr_number
            elif curr_operand == "||":
                result = int(str(result) + str(curr_number))
            else:
                raise ValueError
        if result == value:
            print("We got em, boys")
            adds_up = True
            break

    if adds_up:
        good_ones.append(value)

print(sum(good_ones))
