with open("input") as lines:
    for line in lines:
        input = [int(x) for x in line.strip().split(" ")]


print(input)


def complete_round(curr):
    next = []
    for v in curr:
        if len(str(v)) % 2 == 0:
            str_v = str(v)
            halfway_i = int(len(str_v) / 2)
            left = int(str_v[0:halfway_i])
            right = int(str_v[halfway_i:])
            # print(f"{v=}, splitting {left} and {right}")
            next.append(left)
            next.append(right)
        elif v == 0:
            # print(f"{v=}, to one")
            next.append(1)
        else:
            # print(f"{v=}, multiply")
            next.append(v * 2024)

    # print(f"{next=}")
    return next


rounds = 25
curr = input
for round in range(rounds):
    print(round)
    next = complete_round(curr)
    curr = next

# print(f"Final Arrangement: \n{next}")
print(f"Final Length: {len(next)}")
