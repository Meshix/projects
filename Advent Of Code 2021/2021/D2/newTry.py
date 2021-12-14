actions = [l.strip().split(" ") for l in open("input.txt")]
horizontal1, horizontal2, depth1, depth2, aim = 0, 0, 0, 0, 0
functions = {"forward": lambda n: (horizontal1 + n, depth1, horizontal2 + n, depth2 + aim * n, aim),
             "down": lambda n: (horizontal1, depth1 + n, horizontal2, depth2, aim + n),
             "up": lambda n: (horizontal1, depth1 - n, horizontal2, depth2, aim - n)}
for action in actions:
    horizontal1, depth1, horizontal2, depth2, aim = functions[action[0]](int(action[1]))
print(horizontal1 * depth1, horizontal2 * depth2)