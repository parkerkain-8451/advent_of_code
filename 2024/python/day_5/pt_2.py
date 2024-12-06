rules = {}
updates = []

reading_first_section = True
with open("input") as lines:
    for line in lines:
        line = line.strip()
        if line == "":
            # print("Second section!")
            reading_first_section = False
            continue

        if reading_first_section:
            k, v = line.split("|")
            if int(k) not in rules:
                rules[int(k)] = [int(v)]
            else:
                rules[int(k)].append(int(v))

        if not reading_first_section:
            pages = [int(x) for x in line.split(",")]
            updates.append(pages)


print(rules)
# print(updates)

good_updates = []
bad_updates = []
for curr_update in updates:
    curr_good = True
    for i in range(1, len(curr_update)):
        curr_page = curr_update[i]
        curr_rules = rules.get(curr_page, [])
        prior_pages = curr_update[0:i]
        if len(set(prior_pages).intersection(set(curr_rules))) > 0:
            curr_good = False
            break
    if curr_good:
        # print(f"Update is good! {curr_update}")
        good_updates.append(curr_update)
    else:
        # print(f"Update is bad! {curr_update}")
        bad_updates.append(curr_update)

# result = sum([x[int(len(x) / 2)] for x in good_updates])
# print(f"Final Answer: {result}")

print(bad_updates)
fixed_updates = []


def fix_update(update):
    # print(f"Update before fix: {update}")
    no_fix_applied = True
    for i in range(1, len(update)):
        curr_page = update[i]
        curr_rules = rules.get(curr_page, [])
        prior_pages = update[0:i]
        intersection = set(prior_pages).intersection(set(curr_rules))
        if len(intersection) > 0:
            # print(intersection)
            broken_rules_i = [update.index(x) for x in intersection]
            # print(broken_rules_i)
            swap_index = min(broken_rules_i)
            tmp = update[swap_index]
            update[swap_index] = curr_page
            update[i] = tmp
            # print(f"Update after fix: {update}")
            no_fix_applied = False
            break
    if no_fix_applied:
        # print("No Fix applied - exiting")
        return update
    else:
        # print("Fix applied - looping")
        return fix_update(update)


for curr_update in bad_updates:
    fixed_update = fix_update(curr_update)
    # print(f"Update after exiting fix method: {fixed_update}")
    fixed_updates.append(fixed_update)


print(fixed_updates)
result = sum([x[int(len(x) / 2)] for x in fixed_updates])
print(f"Final Answer: {result}")
