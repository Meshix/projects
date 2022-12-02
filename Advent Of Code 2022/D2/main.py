# load content from input.txt
with open(r'd2/matches.txt', "r") as f:
    content = f.readlines()

# part 1

# remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# create tuples from every string in content
content = [tuple(x.split(' ')) for x in content]

wins = [("A", "Y"), ("B", "Z"), ("C", "X")]
draws = [("A", "X"), ("B", "Y"), ("C", "Z")]
points = {"X": 1, "Y": 2, "Z": 3}

score = 0

for match in content:
    if match in wins:
        score += 6
    elif match in draws:
        score += 3
    score += points[match[1]]

print(score)

# part 2

wins = {"A": 2, "B": 3, "C": 1}
draws = {"A": 1, "B": 2, "C": 3}
loses = {"A": 3, "B": 1, "C": 2}

score = 0

for match in content:
    if match[1] == "X":
        score += loses[match[0]]
    elif match[1] == "Y":
        score += draws[match[0]] + 3
    elif match[1] == "Z":
        score += wins[match[0]] + 6

print(score)