from typing import Any
import numpy as np
from operator import itemgetter
from datetime import datetime

# Get all maps into some data structure
f = open("input_smol", "r")
lines = f.readlines()

seeds = []
lookups: dict[str, Any] = {}
curr_map = ""
for curr_line in lines:
    curr_line = curr_line.replace("\n", "")
    if curr_line.startswith("seeds:"):
        pieces = [int(x) for x in curr_line.replace("seeds: ", "").split(" ")]
        while len(pieces) > 0:
            start = pieces.pop(0)
            length = pieces.pop(0)
            seeds.append((start, start+length-1))
    else:
        if len(curr_line) == 0:
            continue
        elif curr_line[0].isalpha():
            curr_map = curr_line.split(" ")[0]
            lookups[curr_map] = []
        else:
            lookups[curr_map].append([int(x) for x in curr_line.split(" ")])

# print(seeds)
# print(lookups)

def make_bounds(lookup):
    bounds = []
    lookup = sorted(lookup, key=itemgetter(1))
    # print(lookup)
    bounds.append([0, lookup[0][1], 0])
    curr_lb = lookup[0][1]
    for curr_lkp in lookup:
        bounds.append([curr_lb, curr_lb + curr_lkp[2], curr_lkp[0] - curr_lkp[1]])
        curr_lb = curr_lb + curr_lkp[2]
    bounds.append([bounds[-1][1], np.inf, 0])
    return bounds

def apply_input_to_bounds(bounds, seeds):
    new_bounds = []
    for curr_bound in bounds:
        useful_lb = curr_bound[0]
        useful_ub = curr_bound[1]
        for curr_seed in seeds:
            print(curr_seed) 
        new_bounds.append([useful_lb, useful_ub, curr_bound[2]])
    return new_bounds

bounds = make_bounds(lookups["seed-to-soil"])
updated_bounds = apply_input_to_bounds(bounds, seeds)
print(bounds)
print(updated_bounds)
