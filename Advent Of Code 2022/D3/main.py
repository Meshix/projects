# get list of strings from input.txt

def get_input():
    with open('D3/input.txt', 'r') as f:
        return f.read().splitlines()

rucksacks = get_input()

same_itmes = []

# part 1

for compartment in rucksacks:
    first_part = set(compartment[:len(compartment)//2])
    second_part = set(compartment[len(compartment)//2:])
    for c in first_part:
        if c in second_part:
            same_itmes.append(c)

priorities = 0
for item in same_itmes:
    if item.islower():
        priorities += ord(item) - 96
    else:
        priorities += ord(item) - 38
print(priorities)

# part 2

common_items = []
for rucksack in range(0, len(rucksacks), 3):
    common_items.append(set(rucksacks[rucksack]) & set(rucksacks[rucksack+1]) & set(rucksacks[rucksack+2]))

# common_items to list
common_items = [list(item) for item in common_items]
common_items = [item for sublist in common_items for item in sublist]

priorities = 0
for item in list(common_items):
    if item.islower():
        priorities += ord(item) - 96
    else:
        priorities += ord(item) - 38
print(priorities)