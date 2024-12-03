import re

total = 0
with open("input") as lines:
    for line in lines:
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
        # print(matches)
        for match in matches:
            first, second = match.split(",")
            first = int(first[4:])
            second = int(second[:-1])
            # print(first, second)
            total += first * second

print(f"Final Answer: {total}")
