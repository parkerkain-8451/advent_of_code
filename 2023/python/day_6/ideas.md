for a given race:

time = t
distance = d
x = how long to hold

for a race of 7 seconds 
t = 7
d = (t - x) * (x)

if x is 1:
d = (7 - 1) * 1 = 6

if the current_record is r:

we need to solve:
r > (t - x) * x

for t = 7 and r = 9
9 > (7 - x) * x
for 0 >= x >= t

x=0: 9 < (7 - 0) * 0, false
x=1: 9 < (7 - 1) * 1, false
x=2: 9 < (7 - 2) * 2, true
x=3: 9 < (7 - 3) * 3, true
...
x=t: 9 < (7 - 7) * 7, false

9 < 7x - x^2
0 < -x^2 + 7x - 9

-b += sqrt((b^2 -4ac) / 2a)

(7/2) - (1/2)sqrt(13) < x < (7/2) + (1/2)sqrt(13)
1.7 < x < 5.3

how many ints are in this range?
2, 3, 4, 5
and that's ther right answer!


Quatratic generically
r < tx - x^2
or 
-x^2 + tx - r
so, pseudocode:
```
races = read_input("input")

answers = []
for t, r in races:
    bounds = solve_quadratic(a=-1, b=t, c=-r)
    answer = count_ints_between_bounds(bounds)
    answers.append(answer)

final = 1
final = final * x for x in answers
```

