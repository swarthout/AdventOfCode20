from dataclasses import dataclass


@dataclass
class Instruction:
    op: str
    arg: int
    visited: bool


def parse_input(filename):
    program = []
    with open(filename) as f:
        for line in f.readlines():
            op, arg = line.strip().split(" ")
            program.append(Instruction(op, int(arg), False))
    return program


def problem_1():
    program = parse_input("input.txt")
    terminates, accumulator = run_program(program)
    return accumulator


def run_program(program):
    accumulator = 0
    program_counter = 0
    program_len = len(program)
    terminates = False
    while True:
        if program_counter >= program_len:
            terminates = True
            break
        instruction = program[program_counter]
        if instruction.visited:
            terminates = False
            break
        program[program_counter].visited = True
        if instruction.op == "nop":
            program_counter += 1
        elif instruction.op == "acc":
            accumulator += instruction.arg
            program_counter += 1
        elif instruction.op == "jmp":
            program_counter += instruction.arg
    return terminates, accumulator


def problem_2():
    program = parse_input("input.txt")
    for i, instruction in enumerate(program):
        old_op = instruction.op
        new_op = None
        if instruction.op == "acc":
            continue
        elif instruction.op == "nop":
            new_op = "jmp"
        elif instruction.op == "jmp":
            new_op = "nop"
        program[i].op = new_op
        terminates, accumulator = run_program(program)
        if terminates:
            return accumulator
        program[i].op = old_op
        for x in range(len(program)):
            program[x].visited = False
    return None


def main():
    res = problem_1()
    print(res)
    res = problem_2()
    print(res)


if __name__ == "__main__":
    main()
