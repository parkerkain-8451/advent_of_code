input = []

with open("input") as lines:
    for line in lines:
        input.append([int(x) for x in line.split(" ")])


def process_line(line: list[int]):
    is_increasing = line[0] < line[1]

    for i in range(1, len(line)):
        curr = line[i]
        prev = line[i - 1]
        if is_increasing and ((curr - prev) <= 3) and (curr > prev):
            continue
        elif not is_increasing and ((prev - curr) <= 3) and (prev > curr):
            continue
        else:
            return False

    return True


safe_reports = 0
for line in input:
    safe_reports += process_line(line)
print(f"Final Answer: {safe_reports}")
