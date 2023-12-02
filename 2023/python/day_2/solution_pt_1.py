import re

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

f = open("input", "r")
lines = f.readlines()

# lines = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

answer = 0
for i, curr_line in enumerate(lines):
    to_add = (i+1)

    # Split line
    content = curr_line.split(":")[1].replace("\n", "")
    rounds = re.split(",|;", content)

    for curr_round in rounds:
        amt, color = curr_round[1:].split(" ")
        if int(amt) > maxes[color]:
            print(f"amt {amt} is too much for color {color}")
            to_add = 0
            break
    answer += to_add
print(f"Final Answer: {answer}")
