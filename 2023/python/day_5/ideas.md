So what I think I need to do is forget the seeds until the end.

The issue is if i try to work backwards, the answer is just "well, I need a humidity that maps to 0, or 1, or 2, etc.", since everything is a range and I don't know what my inputs are.

Is there a way for me to process the inputs in bulk?

if I have the range [79, 10], [91, 10]
which is really [79, 89] and [91, 101]

and the maps 
[52, 50, 48]
[50, 98, 2]

I can maybe make the latter like a complete mapping of i to o?

second bound is exclusive
[0, 50, i]
[50, 98, i+2]
[98, 100, i-48]
[101, infinity, i]

Then applying the input to this i get
[79, 89, i+2]
[91, 98, i+2]
[98, 101, i-48]

how do i know this? 
Well, 0 to 50 covers none of the ranges so get rid of it
the 50 to 98 range shows up in 79 to to 89 and 91 to 101
    * 98 - 79 > 0, and covers the numbers 79 to min(89, 98) so 79 to 89
    * 


THEN, when I move onto the next mapping
[49, 53, 8]
[0, 11, 42]
[42, 0, 7]
[57, 7, 4]

I can ignore things not in my input. Mapping again:
[0, 7, i+42]
[7, 11, i+50]
[11, 53, i-11]
[53, 61, i-4]
[62, infinity, i]

Then apply my current input:
[79, 93, i+2]

And we can keep going, but ASSUMING this was the end, all I have to is get the min of all of my ranges and I'm done, right?

# Is this going to be fast enough
Will there be too many intersection points between my input and ranges? I have no idea :)

# Ignore the input mapping

[0, 50, i]
[50, 98, i+2]
[98, 100, i-48]
[101, infinity, i]

then 
[0, 7, i+42]
[7, 11, i+50]
[11, 53, i-11]
[53, 61, i-4]
[62, infinity, i]
