# Read input
f = open("input", 'r')
lines = f.readlines()

input: list[int] = []
for line in lines:
    curr_val = int(line)
    if curr_val < 2020:
        input.append(curr_val)

# A little sample input
# input = [1721, 979, 366, 299, 675, 1456]
# print(f"Filtered input: {input}")

# Now, two pointers 
for i, i_val in enumerate(input):
    for j_val in input[i+1:]:
        if (i_val + j_val) == 2020:
            print(f"i: {i_val}, j: {j_val}")
            print(f"Solution is {i_val * j_val}")
            break
