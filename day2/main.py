from dataclasses import dataclass


@dataclass
class PasswordPolicy:
    first_pos: int
    second_pos: int
    letter: str
    password: str


def problem_1():
    passwords = get_lines()
    i = 0
    for password in passwords:
        if is_valid_part_1(password):
            i += 1
    return i


def problem_2():
    passwords = get_lines()
    i = 0
    for password in passwords:
        if is_valid_part_2(password):
            i += 1
    return i


def get_lines():
    passwords = []
    with open("input.txt") as f:
        for line in f.readlines():
            i = line.find("-")
            first_pos = int(line[:i])
            line = line[i + 1:]
            i = line.find(" ")
            second_pos = int(line[:i])
            letter = line[i + 1]
            password = line[i + 4:-1]
            passwords.append(PasswordPolicy(first_pos, second_pos, letter, password))
    return passwords


def is_valid_part_1(password: PasswordPolicy):
    count = password.password.count(password.letter)
    return password.first_pos <= count <= password.second_pos


def is_valid_part_2(password: PasswordPolicy):
    if len(password.password) < password.first_pos:
        return False
    if len(password.password) < password.second_pos:
        return False
    first_pos_match = password.password[password.first_pos - 1] == password.letter
    second_pos_match = password.password[password.second_pos - 1] == password.letter
    is_valid = first_pos_match ^ second_pos_match
    return is_valid


def main():
    answer = problem_1()
    print(answer)
    answer = problem_2()
    print(answer)


if __name__ == "__main__":
    main()
