from day1 import read_text


def clean_line(line):
    """Reads line, separates into instruction, first coordinate, second coordinate.
    0 is off, 1 is on, 2 is toggle"""

    separate_numbers = line.split(',')

    first_coordinate = (int(separate_numbers[0].split(' ')[-1]), int(separate_numbers[1].split(' ')[0]))
    second_coordinate = (int(separate_numbers[1].split(' ')[-1]), int(separate_numbers[2].split(' ')[0]))
    instruction = separate_numbers[0].split(' ')
    if len(instruction) == 3:
        if len(instruction[1]) == 3:
            instruction = 0
        else:
            instruction = 1
    else:
        instruction = 2

    return (instruction, first_coordinate, second_coordinate)


def lets_light(lines: list):
    """follow instruction"""

    on = set()

    for line in lines:
        instruction, first, second = clean_line(line)
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                if instruction == 0:
                    if (x,y) in on:
                        on.remove((x,y))
                if instruction == 1:
                    on.add((x,y))
                if instruction == 2:
                    if (x,y) in on:
                        on.remove((x,y))
                    else:
                        on.add((x,y))
    return len(on)


def lets_increase(lines: list):
    """follow instruction"""

    on = {}

    for i, line in enumerate(lines):
        instruction, first, second = clean_line(line)
        for x in range(first[0], second[0] + 1):
            for y in range(first[1], second[1] + 1):
                if instruction == 0:
                    if (x,y) in on.keys():
                        value = on[(x,y)]
                        if value > 0:
                            on[(x,y)] = value - 1
                if instruction == 1:
                    if (x,y) in on.keys():
                        value = on[(x,y)]
                        on[(x,y)] = value+ 1
                    else:
                        on[(x,y)] = 1
                if instruction == 2:
                    if (x,y) in on.keys():
                        value = on[(x,y)]
                        on[(x,y)] = value + 2
                    else:
                        on[(x,y)] = 2
        print(i)

    return sum(on.values())



if __name__ == "__main__":
    instructions = read_text("day6.txt")
    print(lets_increase(instructions))