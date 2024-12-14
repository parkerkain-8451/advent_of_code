inputs = []
import time

bounds = (101, 103)
# bounds = (11, 7)

with open("input") as lines:
    for line in lines:
        p, v = line.strip().split(" ")
        p = p.replace("p=", "").split(",")
        p = (int(p[0]), int(p[1]))
        v = v.replace("v=", "").split(",")
        v = (int(v[0]), int(v[1]))
        inputs.append({"p": p, "v": v})


def get_state(t):
    final_state = []
    for i in inputs:
        p = i["p"]
        v = i["v"]
        new_p = p[0] + v[0] * t, p[1] + v[1] * t
        # print(f"Before Wrap: {new_p=}")
        new_p = new_p[0] % (bounds[0]), new_p[1] % (bounds[1])
        # print(f"After Wrap: {new_p=}")
        final_state.append(new_p)
    return final_state


def summarize_streaks(state):
    biggest_streak = 0
    for i in range(0, int(bounds[0] / 2)):
        curr_streak = 0
        for j in range(0, bounds[1]):
            if (i, j) in state:
                curr_streak += 1
            else:
                if curr_streak > biggest_streak:
                    biggest_streak = curr_streak
                curr_streak = 0

    for j in range(0, int(bounds[1] / 2)):
        curr_streak = 0
        for i in range(0, bounds[0]):
            if (i, j) in state:
                curr_streak += 1
            else:
                if curr_streak > biggest_streak:
                    biggest_streak = curr_streak
                curr_streak = 0
    return biggest_streak


def draw_grid(state):
    for j in range(0, bounds[1]):
        curr_row = ""
        for i in range(0, bounds[0]):
            # print(f"Looking for {(i, j)}")
            if (i, j) in state:
                curr_row += "X"
            else:
                curr_row += "."
        print(curr_row)


# t = 8270
# state = get_state(t)
# streak = summarize_streaks(state)
# draw_grid(state)
for t in range(0, 1000000):
    state = get_state(t)
    streak = summarize_streaks(state)
    if t % 100 == 0:
        print(f"{t=}, {streak=}")
    if streak > 5:
        print(f"{t=}, {streak=}")
        draw_grid(state)
        time.sleep(5)
