import re
import math

f = open("input", "r")
lines = f.readlines()
# lines = [
#     "Time:      7  15   30",
#     "Distance:  9  40  200",
# ]

cleaned_lines = []
for curr_line in lines:
    cleaned_line = re.split(" +", curr_line.replace("\n", ""))[1:]
    cleaned_line_single = "".join(cleaned_line)
    cleaned_lines.append([int(cleaned_line_single)])


def solve_quadratic(a, b, c):
    solution_1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    solution_2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return solution_1, solution_2


answers = []
final_answer = 1
for t, r in zip(cleaned_lines[0], cleaned_lines[1]):
    print("======================")
    print(t, r)
    lb, ub = solve_quadratic(a=-1, b=t, c=-r)
    print(lb, ub)
    solutions = range(math.ceil(lb), math.floor(ub) + 1)
    num_solutions = len(solutions)
    if round(lb - math.ceil(lb), 4) == 0:
        num_solutions -= 1
    if round(ub - math.ceil(ub), 4) == 0:
        num_solutions -= 1
    
    print(solutions)
    print(num_solutions )
    answers.append(num_solutions)
    final_answer = final_answer * num_solutions

print(answers)
print(f"Part One Answer: {final_answer}")
