from typing import Any

# Get all maps into some data structure
f = open("input", "r")
lines = f.readlines()

seeds = []
lookups: dict[str, Any] = {}
curr_map = ""
for curr_line in lines:
    curr_line = curr_line.replace("\n", "")
    if curr_line.startswith("seeds:"):
        seeds = [int(x) for x in curr_line.replace("seeds: ", "").split(" ")]
    else:
        if len(curr_line) == 0:
            continue
        elif curr_line[0].isalpha():
            curr_map = curr_line.split(" ")[0]
            lookups[curr_map] = []
        else:
            lookups[curr_map].append([int(x) for x in curr_line.split(" ")])

print(seeds)
print(lookups)

# lookup(79, seed-to-soil)
# This iterates through, says the second row is the one containing 79
# We know this bc 50 + 48 > 79
# 79 - 50 = 29, so return 52 + 29 = 81

# lookup(81, soil-to-fertilizer)
# Iterates through, finds nothing
# Return 81


def lookup(id, table_name, lookups):
    for curr_row in lookups[table_name]:
        if curr_row[1] <= id < curr_row[1] + curr_row[2]:
            return curr_row[0] + (id - curr_row[1])
    return id


locations = []
for curr_seed in seeds:
    id = curr_seed
    for curr_lookup in lookups:
        id = lookup(id, curr_lookup, lookups)
    locations.append(id)

# Repeat, after humidity-to-location, store the answer!
# Get min of this list
print(locations)
print(f"Part One Answer is: {min(locations)}")
