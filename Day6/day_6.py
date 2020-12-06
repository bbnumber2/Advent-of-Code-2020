import time

raw_input = open('puzzle_input_6.txt', 'r')
puzzle_input = []
group = []
for line in raw_input:
    if line == '\n':
        puzzle_input.append(group)
        group = []
        continue
    line = line.strip()
    group.append(line)
else:
    puzzle_input.append(group)

PART = 2
def main(puzzle_input):
    if PART == 1:
        question_sum = 0
        for group in puzzle_input:
            questions = []
            questions = {letter for person in group for letter in person}
            question_sum += len(questions)
        return question_sum
    elif PART == 2:
        question_sum = 0
        for group in puzzle_input:
            if len(group) == 1:
                question_sum += len(group[0])
                continue
            
            for letter in group[0]:
                for person in group[1:]:
                    if letter in person:
                        continue
                    break
                else:
                    question_sum += 1
        return question_sum


if __name__ == '__main__':
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)