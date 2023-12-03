def perform_search(lines, i, j, curr_part_start, num_rows, num_cols):
    min_i = max(0, i - 1)
    max_i = min(num_rows - 1, i + 1)
    min_j = max(0, curr_part_start - 1)
    max_j = min(num_cols - 1, j)
    # print(min_i, max_i, min_j, max_j)
    for curr_i in range(min_i, max_i + 1):
        for curr_j in range(min_j, max_j + 1):
            # print(f"Searching: {curr_i, curr_j}")
            if not lines[curr_i][curr_j].isdigit() and lines[curr_i][curr_j] != ".":
                # print("Found Symbol!")
                return True
    return False


def solve(lines):
    num_cols = len(lines[0])
    num_rows = len(lines)
    # print(num_cols, num_rows)
    result = 0
    for i in range(num_rows):
        # Initialize some values
        curr_part_start = -999
        curr_part_no = ""
        for j in range(num_cols):
            curr_char = lines[i][j]

            # If a digit, keep storing
            if curr_char.isdigit():
                curr_part_no += curr_char
                if curr_part_start == -999:
                    curr_part_start = j
                if j == num_cols - 1:
                    # If on the last column, go ahead and check
                    # print(f"Beginning search around part: {curr_part_no}")
                    found_symbol = perform_search(
                        lines, i, j, curr_part_start, num_rows, num_cols
                    )
                    if found_symbol:
                        result += int(curr_part_no)

            # If not a digit, see if our number has a symbol around it
            elif curr_part_start != -999:
                # print(f"Beginning search around part: {curr_part_no}")
                found_symbol = perform_search(lines, i, j, curr_part_start, num_rows, num_cols)
                if found_symbol:
                    result += int(curr_part_no)
                curr_part_start = -999
                curr_part_no = ""

    return result


f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]
# print(lines)
print(solve(lines))
