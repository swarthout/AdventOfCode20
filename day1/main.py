from itertools import combinations


def problem_1():
    lines = get_lines()
    for x, y in combinations(lines, 2):
        if x + y == 2020:
            return x * y


def get_lines():
    with open("input.txt") as f:
        lines = [int(num) for num in f.readlines()]
    return lines


def problem_2():
    lines = get_lines()
    for x, y, z in combinations(lines, 3):
        if x + y + z == 2020:
            return x * y * z


def main():
    answer = problem_1()
    print(answer)
    answer = problem_2()
    print(answer)


if __name__ == "__main__":
    main()
