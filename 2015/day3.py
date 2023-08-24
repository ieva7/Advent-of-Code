from day1 import read_text

def grid_functoin(line: str) -> int:
    been_to = {(0,0)}
    x = 0
    y = 0
    for step in range(0, len(line), 2):
        if line[step] == '>':
            x += 1
        elif line[step] == '<':
            x -= 1
        elif line[step] == "^":
            y += 1
        else:
            y -= 1
        been_to.add((x, y))

    x = 0
    y = 0

    for step in range(1, len(line), 2):
        if line[step] == '>':
            x += 1
        elif line[step] == '<':
            x -= 1
        elif line[step] == "^":
            y += 1
        else:
            y -= 1
        been_to.add((x, y))

    return len(been_to)


if __name__ == "__main__":

    file = read_text("day3.txt")
    print(grid_functoin(file[0]))