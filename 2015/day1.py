SANTA = "input.txt"

def read_text(filepath: str) -> list:
    with open(filepath) as f:
        lines = f.readlines()
    return lines


def find_floor(line: str) -> int:
    up = line.count('(')
    down = line.count(')')
    return up-down


def find_minus_one(line:str) -> int:
    floor = 0
    for count, char in enumerate(line):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return count+1
    else: return 0


if __name__ == "__main__":

    file = read_text(SANTA)
    print(find_floor(file[0]))
    print(find_minus_one(file[0]))
