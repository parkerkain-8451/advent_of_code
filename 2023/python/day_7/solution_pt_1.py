f = open("input", "r")
raw = f.readlines()
# raw = [
#     "32T3K 765",
#     "T55J5 684",
#     "KK677 28",
#     "KTJJT 220",
#     "QQQJA 483",
# ]
lines = [x.split() for x in raw]
print(lines)

card_values = {
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "T": "10",
    "J": "11",
    "Q": "12",
    "K": "13",
    "A": "14",
}


def get_hand_rank(hand):

    counts_dict = {}
    for c in hand: 
        if c in counts_dict.keys():
            counts_dict[c] += 1
        else:
            counts_dict[c] = 1

    counts = list(counts_dict.values())
    counts.sort()
    max_count = max(counts)
    min_count = min(counts)

    if max_count == 5:
        return '7'
    elif max_count == 4:
        return '6'
    elif max_count == 3 and min_count == 2:
        return '5'
    elif max_count == 3:
        return '4'
    elif counts == [1, 2, 2]:
        return '3'
    elif max_count == 2:
        return '2'
    return '1'

# Let's give every hand a score.
def score_hand(hand):
    """Assign every card a 11 digit number according to it's rank"""

    slot_0 = card_values[hand[0]]
    slot_1 = card_values[hand[1]]
    slot_2 = card_values[hand[2]]
    slot_3 = card_values[hand[3]]
    slot_4 = card_values[hand[4]]

    hand_rank = get_hand_rank(hand)

    score = int(hand_rank + slot_0 + slot_1 + slot_2 + slot_3 + slot_4)
    return score

scores = [score_hand(h) for h, _ in lines]
ranks = [sorted(scores).index(h) + 1 for h in scores]
# print(scores)
# print(ranks)

result_list = []
for h, r in zip(lines, ranks):
    bid = h[1]
    result_list.append(int(bid) * r)

print(f"Part one answer: {sum(result_list)}")
    
