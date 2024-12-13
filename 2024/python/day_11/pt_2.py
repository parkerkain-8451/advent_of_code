from collections import Counter

with open("input") as lines:
    for line in lines:
        input = [int(x) for x in line.strip().split(" ")]
        input = dict(Counter(input))

print(input)


def inc_or_add(next, k, reps):
    if k in next:
        next[k] += reps
    else:
        next[k] = reps

    return next


def complete_round(curr):
    next = {}

    for k, v in curr.items():
        # print(k, v)
        if len(str(k)) % 2 == 0:
            str_k = str(k)
            halfway_i = int(len(str_k) / 2)
            left = int(str_k[0:halfway_i])
            right = int(str_k[halfway_i:])
            # print(f"{k=}, splitting {left} and {right}")
            next = inc_or_add(next, left, v)
            next = inc_or_add(next, right, v)
        elif k == 0:
            # print(f"{k=}, to one")
            next = inc_or_add(next, 1, v)
        else:
            # print(f"{k=}, multiply")
            next = inc_or_add(next, k * 2024, v)
    return next


rounds = 500
curr = input
for round in range(rounds):
    # print(f"===========================")
    # print(f"Round: {round}")
    next = complete_round(curr)
    # print(next)
    curr = next

# print(f"Final Arrangement: \n{next}")
print(f"Final Length: {sum([x for x in next.values()])}")
