inputs = []
bounds = (101, 103)
t = 100

with open("input") as lines:
    for line in lines:
        p, v = line.strip().split(" ")
        p = p.replace("p=", "").split(",")
        p = (int(p[0]), int(p[1]))
        v = v.replace("v=", "").split(",")
        v = (int(v[0]), int(v[1]))
        inputs.append({"p": p, "v": v})

final_state = []
for i in inputs:
    p = i["p"]
    v = i["v"]
    new_p = p[0] + v[0] * t, p[1] + v[1] * t
    # print(f"Before Wrap: {new_p=}")
    new_p = new_p[0] % (bounds[0]), new_p[1] % (bounds[1])
    # print(f"After Wrap: {new_p=}")
    final_state.append(new_p)

print(sorted(final_state))

middle_x = int((bounds[0] - 1) / 2)
middle_y = int((bounds[1] - 1) / 2)

quad_1 = sum(1 for x in final_state if x[0] > middle_x and x[1] < middle_y)
print(f"{quad_1=}")
quad_2 = sum(1 for x in final_state if x[0] < middle_x and x[1] < middle_y)
print(f"{quad_2=}")
quad_3 = sum(1 for x in final_state if x[0] < middle_x and x[1] > middle_y)
print(f"{quad_3=}")
quad_4 = sum(1 for x in final_state if x[0] > middle_x and x[1] > middle_y)
print(f"{quad_4=}")

final_answer = quad_1 * quad_2 * quad_3 * quad_4
print(f"Final Answer: {final_answer}")
