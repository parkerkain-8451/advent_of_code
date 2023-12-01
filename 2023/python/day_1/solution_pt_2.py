f = open("input", "r")
lines = f.readlines()
# lines = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

valid_nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

running_sum = 0

for curr_line in lines:

    first_dig = None
    first_dig_buf = ""
    last_dig = None
    last_dig_buf = ""

    # loop through string
    for i in range(len(curr_line)):

        if curr_line[i].isdigit() and not first_dig:
            first_dig = curr_line[i]
        elif not first_dig:
            # build a string buffer to search for int names
            first_dig_buf += curr_line[i]

            # There has to be a better way to do this - 
            # Seach the substrings of the buffer for valid 
            # numbers
            for start in range(len(first_dig_buf)):
                curr_first_dig_buf = first_dig_buf[start:]
                if curr_first_dig_buf in valid_nums.keys():
                    first_dig = valid_nums[curr_first_dig_buf]

        # Loop backwards using the same pointer
        last_dig_to_check = -(i + 1)
        if curr_line[last_dig_to_check].isdigit() and not last_dig:
            last_dig = curr_line[last_dig_to_check]
        elif not last_dig:
            last_dig_buf = curr_line[last_dig_to_check] + last_dig_buf
            for end in range(len(last_dig_buf), 0, -1):
                curr_last_dig_buf = last_dig_buf[:end]
                if curr_last_dig_buf in valid_nums.keys():
                    last_dig = valid_nums[curr_last_dig_buf]

        # Resolve if we find both digits
        if first_dig and last_dig:
            value_to_add = int(f"{first_dig}{last_dig}")
            print(value_to_add)
            running_sum += value_to_add
            break

print(f"Final Sum: {running_sum}")
