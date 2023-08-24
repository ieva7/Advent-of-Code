from day1 import read_text


class Action:

    def __init__(self, input) -> None:
        self.input = input


    def get_value(self):
        return self.value

    def calculate_value(self):

        if
        if self.operation == "OR":
            return self.input


def finding_output(input_file: list):

    elements = {}

    for line in input_file:
        line = line.strip()
        first_split = line.split(" -> ")
        second_split = first_split[0].split(' ')
        print(elements)
        print(second_split)

        if len(second_split) == 1:
            elements[first_split[1]] = int(first_split[0])
        if len(second_split) == 2:
            elements[first_split[1]] = ~int(elements[second_split[1]])
        if len(second_split) == 3:
            first_elem = elements[second_split[0]]
            if second_split[1] == "AND":
                second_elem = elements[second_split[2]]
                elements[first_split[1]] = first_elem & second_elem
            if second_split[1] == "OR":
                second_elem = elements[second_split[2]]
                elements[first_split[1]] = first_elem | second_elem
            if second_split[1] == "RSHIFT":
                second_elem = int(second_split[2])
                elements[first_split[1]] = first_elem >> second_elem
            if second_split[1] == "LSHIFT":
                second_elem = int(second_split[2])
                elements[first_split[1]] = first_elem << second_elem
    return elements


if __name__ == "__main__":

    input_1 = read_text("day7.txt")
    print(finding_output(input_1)['a'])






