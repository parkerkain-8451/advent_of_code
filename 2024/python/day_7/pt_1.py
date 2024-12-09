import re
import itertools as it
import more_itertools as mit


input = []
with open("input") as lines:
    for line in lines:
        parts = re.split(r": | ", line)
        input.append([int(parts[0]), [int(x) for x in parts[1:]]])

# print(input)

good_ones = []
for value, numbers in input:
    # print(value, numbers)
    adds_up = False

    operators = ["+", "*"]
    all_perms = []
    for plusses, multipliers in zip(
        range(0, len(numbers)), range(len(numbers) - 1, -1, -1)
    ):
        all_perms += mit.distinct_permutations(
            (["+"] * plusses) + (["*"] * multipliers)
        )
    # print(list(all_perms))

    for curr_perm in all_perms:
        result = numbers[0]
        for curr_number, curr_operand in zip(numbers[1:], curr_perm):
            # math += f"{curr_number} {curr_operand} "
            if curr_operand == "+":
                result += curr_number
            elif curr_operand == "*":
                result *= curr_number
            else:
                raise ValueError
        # math += str(numbers[-1])
        # # result = eval(math)
        # result = eval(
        #     math,
        #     {"__builtins__": None},
        #     {"*": lambda x, y: x * y, "+": lambda x, y: x + y},
        # )
        # print(math, result)
        if result == value:
            print("We got em, boys")
            adds_up = True
            break

    if adds_up:
        good_ones.append(value)

print(sum(good_ones))
