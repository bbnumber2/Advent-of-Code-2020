# Input
I chose to use a dictionary with the relevant values.
Notably, I also used a, pretty ugly, `new_line := line.replace()...` in order to not retype the line formatting.
There's likely a better way to do this, but I don't know for sure.
# Part 1
This solution is simple because of the dictionary structure.
Generally, I attempt to structure my puzzle data to make part 1 elegantly solvable, which is shown here.
Average runtime of: `600 ns`
# Part 2
This solution is also easily solvable due to the dictionary structure.
Initially, I used an explicit and/or construction.
This was then switched for the more elegant `^` (xor) operator.
Average runtime of `600 ns`
