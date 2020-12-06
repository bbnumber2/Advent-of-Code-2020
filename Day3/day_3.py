import time

raw_input = open('puzzle_input_3.txt', 'r')
puzzle_input = [line for line in raw_input]
PART = 2
def main(puzzle_input):
    if PART == 1:
        x = 0
        max_x = len(puzzle_input[0]) - 1
        tree_count = 0
        for line in puzzle_input:
            if line[x] == '#':
                tree_count += 1
            x += 3
            #Loops puzzle input horizontally
            x %= max_x
        return tree_count
    elif PART == 2:
        max_x = len(puzzle_input[0]) - 1
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        #One to allow multiplication immediately
        tree_count = 1
        for run, rise in slopes:
            x = 0
            slope_trees = 0
            for y, line in enumerate(puzzle_input):
                if y % rise == 1:
                    continue
                if line[x] == '#':
                    slope_trees += 1
                x += run
                #Loops puzzle input horizontally
                x %= max_x
            tree_count *= slope_trees
        return tree_count


if __name__ == "__main__":
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)