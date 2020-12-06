# Input
I planned on using a modulus operator in my solutions, which is why my input is just a `readlines()`
# Part 1
Because the puzzle input repeats infinitely horizontally, the x index can simply loop after it exceeds the maximum.
This operation is succinctly expressed with `x %= max_x`
Average runtime of: `200 ns`
# Part 2
This solution was a more general version of the first one.
I chose to create a list of each slope in order to loop through each of them.
Average runtime of: `600 ns`
