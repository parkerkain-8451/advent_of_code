f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]
# lines = [
#     "LR",
#     "",
#     "11A = (11B, XXX)",
#     "11B = (XXX, 11Z)",
#     "11Z = (11B, XXX)",
#     "22A = (22B, XXX)",
#     "22B = (22C, 22C)",
#     "22C = (22Z, 22Z)",
#     "22Z = (22B, 22B)",
#     "XXX = (XXX, XXX)",
# ]

pattern = lines[0]
pattern = pattern.replace("R", "1").replace("L", "0")

mappings = lines[2:]
map = {}
for m in mappings:
    start, branches = m.split(" = ")
    left, right = branches.split(", ")
    map[start] = [left[1:], right[0:-1]]

print(pattern)
print("============================================")
print(map)

counters = []
for curr_key in map:
    if curr_key.endswith("A"):
        # print(curr_key)
        counter = 0
        location = curr_key
        while not location.endswith("Z"):
            next_pattern = int(pattern[counter % len(pattern)])
            # print(f"at {location} at step {counter}, next pattern is {next_pattern}")
            location = map[location][next_pattern]
            counter += 1
        counters.append(counter)

# print(counters)

# Get least common multiple
min_counter = min(counters)
curr_mult = 1
found_it = False
while not found_it:
    curr_multiple = min_counter * curr_mult
    # print(f"mult: {curr_multiple}")
    for curr_counter in counters:
        curr_div = curr_multiple / curr_counter
        # print(f"div: {curr_div}")
        if not round(int(curr_div) - curr_div, 10) == 0:
            # print("BAD")
            curr_mult += 1
            found_it = False
            break
        found_it = True

print(curr_multiple)
