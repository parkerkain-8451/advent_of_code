import copy

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
    is_safe = process_line(line)
    if is_safe:
        safe_reports += 1
    else:
        for i in range(len(line)):
            line_copy = copy.copy(line)
            line_copy.pop(i)
            is_safe = process_line(line_copy)
            if is_safe:
                safe_reports += 1
                break
print(f"Final Answer: {safe_reports}")
