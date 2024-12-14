import sympy as sp
import re

matricies = []

with open("input") as lines:

    curr_matrix = [[], []]
    for line in lines:
        x_term = re.search(r"X(\+|=)[0-9]+", line)
        if x_term:
            val = int(
                x_term.group(0).replace("X", "").replace("+", "").replace("=", "")
            )
            curr_matrix[0].append(val)
            # print(val)
        y_term = re.search(r"Y(\+|=)[0-9]+", line)
        if y_term:
            val = int(
                y_term.group(0).replace("Y", "").replace("+", "").replace("=", "")
            )
            curr_matrix[1].append(val)
            # print(val)
        if len(curr_matrix[0]) == 3:
            # print(curr_matrix)
            matricies.append(sp.Matrix(curr_matrix))
            curr_matrix = [[], []]


answer = 0
for curr_matrix in matricies:

    print(curr_matrix)
    m_rref, _ = curr_matrix.rref()  # Compute reduced row echelon form (rref).
    print(m_rref)
    a_pushes = m_rref[2]
    b_pushes = m_rref[5]
    if (round(abs(int(a_pushes) - a_pushes), 3) > 0) or (
        round(abs(int(b_pushes) - b_pushes), 3) > 0
    ):
        print(f"Invalid!")
        print("===========================")
        continue
    print(f"Push A {a_pushes} times and B {b_pushes} times")
    cost = 3 * a_pushes + b_pushes
    print(f"Total Cost: {cost}")
    answer += cost
    print("===========================")

print("Final Answer: ", answer)
