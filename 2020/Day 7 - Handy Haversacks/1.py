with open("input.txt") as fp:
    inputs = fp.readlines()

bag_rules = {}
for i in inputs:
    contains_split = i.split('contain')
    outer_bag = contains_split[0].replace(
        'bags', '').replace('bag', '').strip()
    inner_bags = {}
    for j in contains_split[1].split(','):
        space_split = j.strip().split(' ', 1)
        if 'no' not in space_split:
            bag_name = space_split[1].replace('.', '').replace(
                'bags', '').replace('bag', '').strip()
            inner_bags[bag_name] = int(space_split[0])

    bag_rules[outer_bag] = inner_bags


def contains_bag(bag, wanted_bag):
    if wanted_bag in bag_rules[bag]:
        return True

    for sub_bag in bag_rules[bag]:
        if contains_bag(sub_bag, wanted_bag):
            return True


count = 0
for bag in bag_rules:
    if contains_bag(bag, 'shiny gold'):
        count += 1

print(count)
