# part 1
# get input from input.txt and divide it by empty lines

with open('input.txt') as f:
    data = f.read().split('\n\n')

load = []
for elfes in data:
    load.append(elfes.split('\n'))

sums = []
# string list to int list
for i in range(len(load)):
    load[i] = [int(x) for x in load[i]]
    sums.append(sum(load[i]))

print(sorted(sums))

# part 2

print(sum(sorted(sums)[-3:]))