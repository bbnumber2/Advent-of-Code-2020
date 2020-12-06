import time

raw_input = open('puzzle_input_4.txt', 'r')
puzzle_input = []
passport = {}
for line in raw_input:
    if line == '\n':
        puzzle_input.append(passport)
        passport = {}
        continue
    line = line.split()
    for attribute in line:
        key, value = attribute.split(':')
        passport[key] = value
#Appends the final passport
puzzle_input.append(passport)

PART = 2
def main(puzzle_input):
    if PART == 1:
        valid_count = 0
        for passport in puzzle_input:
            if passport.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
                valid_count += 1
        return valid_count
    elif PART == 2:
        valid_count = 0
        hair_colors = '0123456789abcdef'
        eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        for passport in puzzle_input:
            #Try/except to not count failed int conversions
            try:
                if (passport.keys() >= {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}) and \
                (1920 <= int(passport['byr']) <= 2002 and 2010 <= int(passport['iyr']) <= 2020 and 2020 <= int(passport['eyr']) <= 2030) and\
                ((passport['hgt'][-2:] == 'cm' and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and 59 <= int(passport['hgt'][:-2]) <= 76)) and\
                (passport['hcl'][0] == '#' and len(passport['hcl'][1:]) == 6 and all(char in hair_colors for char in passport['hcl'][1:])) and\
                (passport['ecl'] in eye_colors) and\
                (int(passport['pid']) and len(passport['pid']) == 9):
                    valid_count += 1
            except:
                pass
        return valid_count

if __name__ == '__main__':
    start_time = time.time()
    output = main(puzzle_input)
    print(output)
    print(time.time() - start_time)