def parse_input():
    map_matrix = []
    with open("input.txt") as f:
        for line in f.readlines():
            row = [(i == '#') for i in line.strip()]
            map_matrix.append(row)
    return map_matrix


def get_tree_collisions(x_increment, y_increment):
    x, y = 0, 0
    total_trees = 0
    map_matrix = parse_input()
    x_max = len(map_matrix[0])
    y_max = len(map_matrix)
    while y < y_max:
        is_tree = map_matrix[y][x]
        if is_tree:
            total_trees += 1
        x = (x + x_increment) % x_max
        y += y_increment
    return total_trees


def get_all_tree_collisions():
    params = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_product = 1
    for x, y in params:
        total_product *= get_tree_collisions(x, y)
    return total_product


def main():
    answer = get_tree_collisions(3, 1)
    print(answer)
    answer = get_all_tree_collisions()
    print(answer)


if __name__ == "__main__":
    main()
