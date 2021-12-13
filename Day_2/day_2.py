"""solution for day two of advent of code 2021"""
with open('day_2.txt', encoding='utf-8') as file_input:
    file_input = file_input.readlines()
    data = [line.split() for line in file_input]

for i in data:
    i[1] = int(i[1])


def puzzle_1():
    """solution for the first puzzle"""
    horizontal = 0
    depth = 0

    for elem in data:
        if elem[0] == "forward":
            horizontal += elem[1]
        elif elem[0] == "down":
            depth += elem[1]
        elif elem[0] == "up":
            depth -= elem[1]

    print(horizontal * depth)


def puzzle_2():
    """solution for the second puzzle"""
    horizontal = 0
    aim = 0
    depth = 0

    for elem in data:
        if elem[0] == "forward":
            horizontal += elem[1]
            depth += elem[1] * aim
        elif elem[0] == "down":
            aim += elem[1]
        elif elem[0] == "up":
            aim -= elem[1]

    print(horizontal * depth)


puzzle_1()
puzzle_2()
