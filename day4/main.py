import re
from dataclasses import dataclass


@dataclass
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str

    def is_valid(self) -> bool:
        if not (1920 <= self.byr <= 2002):
            return False
        if not (2010 <= self.iyr <= 2020):
            return False
        if not (2020 <= self.eyr <= 2030):
            return False
        units = self.hgt[-2:]
        value = int(self.hgt[:-2])
        if not (units == "cm" or units == "in"):
            return False
        if units == "cm" and not (150 <= value <= 193):
            return False
        if units == "in" and not (59 <= value <= 76):
            return False
        hcl_match = re.fullmatch('#[a-f0-9]{6}', self.hcl)
        if not hcl_match:
            return False
        ecl_match = re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', self.ecl)
        if not ecl_match:
            return False
        pid_match = re.fullmatch('[0-9]{9}', self.pid)
        if not pid_match:
            return False
        return True


def parse_input():
    with open("input.txt") as f:
        input_list = f.read().split("\n\n")
    input_matrix = [p.replace('\n', ' ').split() for p in input_list]
    passports = []
    for p in input_matrix:
        d = {}
        for f in p:
            k, v = f.split(":")
            d[k] = v
        if all_fields_present(d):
            passport = Passport(byr=int(d['byr']),
                                iyr=int(d['iyr']),
                                eyr=int(d['eyr']),
                                hgt=d['hgt'],
                                hcl=d['hcl'],
                                ecl=d['ecl'],
                                pid=d['pid'])
            passports.append(passport)

    return passports


def all_fields_present(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all([field in passport for field in required_fields])


def problem_1():
    passports = parse_input()
    return len(passports)


def problem_2():
    passports = parse_input()
    num_valid = 0
    for p in passports:
        if p.is_valid():
            num_valid += 1
    return num_valid


def main():
    valid_count = problem_1()
    print(valid_count)
    valid_count = problem_2()
    print(valid_count)


if __name__ == "__main__":
    main()
