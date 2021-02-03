def parse_input():
    bag_table = {
        # 'shiny gold': [('dark olive', 2)]
    }
    with open("input.txt") as f:
        for line in f.readlines():
            words = line.split(" ")
            bag_name = " ".join(words[:2])
            inner_bags = []
            words = words[4:]
            if words[0] != 'no':
                for i in range(0, len(words), 4):
                    count, adj, color, _ = words[i:i + 4]
                    inner_bag_name = f"{adj} {color}"
                    count = int(count)
                    inner_bags.append((inner_bag_name, count))
            bag_table[bag_name] = inner_bags
    return bag_table


def find_shiny_gold_bags():
    bag_table = parse_input()
    shiny_gold_count = 0
    target = 'shiny gold'
    for bag in bag_table:
        if bag == target:
            continue
        if contains_target(bag_table, bag, target):
            shiny_gold_count += 1
    return shiny_gold_count


def contains_target(bag_table, start, target):
    to_search = [(start, 0)]
    while to_search:
        next_bag, _ = to_search.pop(0)
        if next_bag == target:
            return True
        else:
            to_search.extend(bag_table[next_bag])
    return False


def count_shiny_gold_bags():
    bag_table = parse_input()
    target = 'shiny gold'
    bag_count = count_inner_bags(bag_table, target)
    return bag_count


def count_inner_bags(bag_table, target):
    bag_count = 0
    to_search = [target]
    while to_search:
        next_bag = to_search.pop(0)
        bag_list = bag_table[next_bag]
        for (bag, count) in bag_list:
            bag_count += count * (count_inner_bags(bag_table, bag) + 1)
    return bag_count


def main():
    res = find_shiny_gold_bags()
    print(res)
    res = count_shiny_gold_bags()
    print(res)


if __name__ == "__main__":
    main()
