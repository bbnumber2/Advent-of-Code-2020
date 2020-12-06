import time

raw_input = open('puzzle_input_2.txt', 'r')
puzzle_input = [{'min': int(new_line[0]), 'max': int(new_line[1]), 'letter': new_line[2], 'password': new_line[3]} for line in raw_input if (new_line := line.replace('-', ' ').replace(':', '').split() or True)]

PART = 2
def main(puzzle_input):
    if PART == 1:
        total_valid = 0
        for password in puzzle_input:
            count = password['password'].count(password['letter'])
            if count >= password['min'] and count <= password['max']:
                total_valid += 1
        return total_valid
    elif PART == 2:
        total_valid = 0
        for password in puzzle_input:
            first_letter = password['password'][password['min'] - 1]
            second_letter = password['password'][password['max'] - 1]
            if (first_letter == password['letter']) ^ (second_letter == password['letter']):
                total_valid += 1
        return total_valid

if __name__ == '__main__':
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)
