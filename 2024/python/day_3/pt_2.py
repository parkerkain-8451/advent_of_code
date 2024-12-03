import re

total = 0
do = True
with open("input") as lines:
    for line in lines:
        matches = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        # print(matches)
        for match in matches:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            else:
                if do:
                    # print(match)
                    first, second = match.split(",")
                    first = int(first[4:])
                    second = int(second[:-1])
                    # print(first, second)
                    total += first * second

print(f"Final Answer: {total}")
