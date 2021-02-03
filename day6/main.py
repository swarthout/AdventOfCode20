def parse_input():
    responses = []
    with open("input.txt") as f:
        group_prefs = f.read().split("\n\n")
        for group in group_prefs:
            prefs_by_person = group.split()
            responses.append(prefs_by_person)

    return responses


def problem_1():
    responses = parse_input()
    total_sum = 0
    for group in responses:
        any_yes = set()
        for person in group:
            for q in person:
                any_yes.add(q)
        total_sum += len(any_yes)

    return total_sum


def problem_2():
    responses = parse_input()
    total_sum = 0
    for group in responses:
        first_person = group[0]
        all_yes = set(list(first_person))
        for person in group:
            person_response = set(list(person))
            all_yes.intersection_update(person_response)
        total_sum += len(all_yes)

    return total_sum


def main():
    valid_count = problem_1()
    print(valid_count)
    valid_count = problem_2()
    print(valid_count)


if __name__ == "__main__":
    main()
