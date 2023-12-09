f = open("input", "r")
lines = f.readlines()
lines = [x.replace("\n", "") for x in lines]

# print(lines)

answers = []
for curr_line in lines:
    rounds = [[int(x) for x in curr_line.split()]]

    # print(rounds[0]) 
    while set(rounds[-1]) != {0}:
        next_round = []
        for i in range(1, len(rounds[-1])):
            next_round.append(rounds[-1][i] - rounds[-1][i - 1])
        rounds.append(next_round)
        # print(next_round)

    predicted = 0
    for i in range(len(rounds)):
        predicted += rounds[i][-1]
    answers.append(predicted)
    # print(predicted)

print(len(answers))
print(f"Part One Answer: {sum(answers)}")
