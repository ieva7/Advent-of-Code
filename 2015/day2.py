from day1 import read_text

PATH = "day2.txt"

def find_area_total(file: list) -> int:
    running_total = 0
    ribbon = 0
    for line in file:
        find_min = numbers = [ int(x) for x in line.split('x') ]
        l = find_min[0]
        w = find_min[1]
        h = find_min[2]
        ribbon += l*h*w
        running_total += 2*l*w + 2*w*h + 2*h*l
        one = min(find_min)
        find_min.remove(one)
        two = min(find_min)
        ribbon += 2*(one+two)
        running_total += one*two
    return running_total, ribbon


if __name__ == "__main__":

    file = read_text(PATH)
    print(find_area_total(file))