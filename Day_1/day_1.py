"""solution for day one of advent of code 2021"""
with open('day_1.txt') as file_input:
    file_input = file_input.readlines()

file_input = [line.strip() for line in file_input]
file_input = [int(i) for i in file_input]


def puzzle_1(data):
    """solution for the first puzzle"""
    counter = sum([1 for i in range(1, len(data)) if data[i] > data[i-1]])
    print(counter)


def puzzle_2():
    """solution for the second puzzle"""
    window = [file_input[i] + file_input[i-1] + file_input[i-2]
              for i in range(2, len(file_input))]
    puzzle_1(window)


puzzle_1(file_input)
puzzle_2()
