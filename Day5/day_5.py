import time

raw_input = open('puzzle_input_5.txt', 'r')
letter_nums = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
puzzle_input = []
for line in raw_input:
    temp_dict = {}
    line = line.strip()
    temp_dict['row'] = int(''.join(letter_nums[letter] for letter in line[:-3]), 2)
    temp_dict['column'] = int(''.join(letter_nums[letter] for letter in line[-3:]), 2)
    puzzle_input.append(temp_dict)
PART = 2
def main(puzzle_input):
    if PART == 1:
        return max(seat['row'] * 8 + seat['column'] for seat in puzzle_input)
    elif PART == 2:
        seats = sorted([seat['row'] * 8 + seat['column'] for seat in puzzle_input])
        for index, seat_id in enumerate(range(seats[0], seats[-1])):
            if seats[index] != seat_id:
                return seat_id

if __name__ == '__main__':
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)