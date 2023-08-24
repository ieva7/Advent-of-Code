from day1 import read_text


def naughty_or_nice(strings: list) -> int:
    nice = 0

    for line in strings:
        overlap_triggered = False
        between_triggered = False
        previous_char = line[0]
        for i, char in enumerate(line):
            if i!= 0 and overlap_triggered is False and previous_char+char in line.replace(previous_char+char, " ", 1):
                overlap_triggered = True
            if between_triggered is False and i!= 0 and i+1 < len(line):
                if line[i+1] == previous_char:
                    between_triggered = True
            previous_char = char
            if between_triggered and overlap_triggered:
                nice += 1
                break
    return nice


if __name__ == "__main__":
    text = read_text("day5.txt")

