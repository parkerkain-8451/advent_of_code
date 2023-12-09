f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]

# print(lines)

answers = []
for curr_line in lines:
    # print("==============================")
    rounds = [[int(x) for x in curr_line.split()]]

    # print(rounds[0]) 
    while set(rounds[-1]) != {0}:
        next_round = []
        for i in range(1, len(rounds[-1])):
            next_round.append(rounds[-1][i] - rounds[-1][i - 1])
        rounds.append(next_round)
        # print(next_round)

    predicted = 0
    for i in range(len(rounds)-2, -1, -1):
        predicted = -predicted + rounds[i][0]
        # print(f"i:{i}, pred: {predicted}")
    answers.insert(0, predicted)

print(answers)
print(len(answers))
print(f"Part Two Answer: {sum(answers)}")
