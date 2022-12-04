# get pairs from D4/input.txt

with(open('D4/input.txt', 'r')) as f:
    pairs = f.read().splitlines()

pairs = [pair.split(',') for pair in pairs]

# part 1
counter = 0
for pair in pairs:
    partner_a = pair[0].split('-')
    partner_b = pair[1].split('-')
    range_a = set(range(int(partner_a[0]), int(partner_a[1])+1))
    range_b = set(range(int(partner_b[0]), int(partner_b[1])+1))
    if range_a.issubset(range_b) or range_b.issubset(range_a):
        counter += 1
print(counter)

# part 2
counter = 0
for pair in pairs:
    partner_a = pair[0].split('-')
    partner_b = pair[1].split('-')
    range_a = set(range(int(partner_a[0]), int(partner_a[1])+1))
    range_b = set(range(int(partner_b[0]), int(partner_b[1])+1))
    if set.intersection(range_a, range_b):
        counter += 1
print(counter)