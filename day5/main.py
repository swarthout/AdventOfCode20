class Seat:
    row: int
    col: int
    id: int

    def calc_row(self, row_str):
        min_row = 0
        max_row = 127
        for letter in row_str:
            if letter == "F":
                max_row = (min_row + max_row) // 2
            elif letter == "B":
                min_row = ((max_row + min_row + 1) // 2)
        assert min_row == max_row
        self.row = min_row

    def calc_col(self, col_str):
        min_col = 0
        max_col = 7
        for letter in col_str:
            if letter == "L":
                max_col = (min_col + max_col) // 2
            elif letter == "R":
                min_col = ((max_col + min_col + 1) // 2)
        assert min_col == max_col
        self.col = min_col

    def __init__(self, row_str, col_str):
        self.calc_row(row_str)
        self.calc_col(col_str)
        self.id = self.row * 8 + self.col


def parse_input():
    seats = []
    with open("input.txt") as f:
        for line in f.readlines():
            row_str = line[:7]
            col_str = line[7:10]
            seat = Seat(row_str=row_str, col_str=col_str)
            seats.append(seat)
    return seats


def problem_1():
    seats = parse_input()
    max_seat = max(seats, key=lambda s: s.id)
    return max_seat.id


def problem_2():
    seats = parse_input()
    sorted_seats = sorted(seats, key=lambda s: s.id)
    for i, seat in enumerate(sorted_seats):
        next_seat = sorted_seats[i + 1]
        if next_seat.id == seat.id + 2:
            return seat.id + 1


def main():
    res = problem_1()
    print(res)
    res = problem_2()
    print(res)


if __name__ == "__main__":
    main()
