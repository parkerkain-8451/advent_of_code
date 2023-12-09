f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]
# lines = [
#     "RL",
#     "",
#     "AAA = (BBB, CCC)",
#     "BBB = (DDD, EEE)",
#     "CCC = (ZZZ, GGG)",
#     "DDD = (DDD, DDD)",
#     "EEE = (EEE, EEE)",
#     "GGG = (GGG, GGG)",
#     "ZZZ = (ZZZ, ZZZ)",
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

counter = 0
location = "AAA"
while location != "ZZZ":
    next_pattern = int(pattern[counter % len(pattern)])
    print(f"at {location} at step {counter}, next pattern is {next_pattern}")
    location = map[location][next_pattern]
    counter += 1
print(counter)

