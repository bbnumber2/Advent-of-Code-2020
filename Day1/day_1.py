import time

raw_input = open('puzzle_input_1.txt')
puzzle_input = [int(line) for line in raw_input]
PART = 2
def main(puzzle_input):
    if PART == 1:
        for num_1 in puzzle_input:
            for num_2 in puzzle_input:
                if num_1 + num_2 == 2020:
                    return num_1 * num_2
    elif PART == 2:
        for num_1 in puzzle_input:
            for num_2 in puzzle_input:
                for num_3 in puzzle_input:
                    if num_1 + num_2 + num_3 == 2020:
                        return num_1 * num_2 * num_3
if __name__ == '__main__':
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)