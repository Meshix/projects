
# Part 1
horizontal = 0
depth = 0
with open("input.txt", "r") as f:
    for line in f:
        action, value = line.split(" ")
        if action[0] == "f":
            horizontal += int(value)
        elif action[0] == "u":
            depth -= int(value)
        else:
            depth += int(value)
print(depth * horizontal)

# Part 2
horizontal = 0
depth = 0
aim = 0
with open("input.txt", "r") as f:
    for line in f:
        action, value = line.split(" ")
        value = int(value)
        if action[0] == "f":
            horizontal += value
            depth += value * aim
        elif action[0] == "u":
            aim -= value
        else:
            aim += value
print(depth * horizontal)

