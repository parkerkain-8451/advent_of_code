f = open("input", "r")
lines = f.readlines()
# lines = [
#     "1abc2",
#     "pqr3stu8vwx",
#     "a1b2c3d4e5f",
#     "treb7uchet",
# ]

running_sum = 0

for curr_line in lines:
    first_dig = None
    last_dig = None
    for i in range(len(curr_line)):
        if curr_line[i].isdigit() and not first_dig:
            first_dig = curr_line[i]

        last_dig_to_check = -(i+1)
        if curr_line[last_dig_to_check].isdigit() and not last_dig:
            last_dig = curr_line[last_dig_to_check]

        if first_dig and last_dig:
            value_to_add = int(f"{first_dig}{last_dig}")
            running_sum += value_to_add 
            break

print(f"Final Sum: {running_sum}")
