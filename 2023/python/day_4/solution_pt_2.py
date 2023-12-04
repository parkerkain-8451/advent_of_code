import re
from typing import Any

f = open("input", "r")
lines = f.readlines()

# lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
# ]
lines = [x.split(": ")[1].replace("\n", "").strip() for x in lines]
# print(lines)

cards = {}
for i, curr_line in enumerate(lines):
    winning_raw, nums_raw = curr_line.split("|")
    winning = set(re.split(" +", winning_raw)[:-1])
    nums = re.split(" +", nums_raw)[1:]
    # print(winning, nums)
    cards[i+1] = (winning, nums)
print(cards)

# Now, get the base wins for each card
base_results = {}
for k, (winning, nums) in cards.items():
    curr_wins = 0
    for num in nums:
        if num in winning:
            curr_wins += 1
    base_results[k] = curr_wins
print(base_results)
    
keys = list(base_results.keys())
keys.sort(reverse = True)
# Iterate through the dict backwards to get out final answers
updated_results: dict[int, Any] = {}
for key in keys:
    new_value = 1
    i = base_results[key]
    while(i > 0):
        new_value += updated_results[key + i]
        i -= 1
    updated_results[key] = new_value
print(updated_results)
print(sum(updated_results.values()))

