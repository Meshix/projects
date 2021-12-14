lines = open("2021/D5/input.txt").read().rstrip().split("\n")
values = []
for line in lines:
    values.append(line.split("->"))

points = [[0] * 1000 for i in range(1000)]

# Part One
for point_pair in values:
    x1, y1 = point_pair[0].split(",")
    x2, y2 = point_pair[1].split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 == x2:
        for y in range(y1, y2):
            points[int(x1)][y] += 1
    else:
        for x in range(int(x1), int(x2)):
            points[x][int(y1)] += 1
flat = [x for sublist in points for x in sublist]
print(len(list(filter(lambda x: x > 1, flat))))
# Part Two
for point_pair in values:
    x1, y1 = point_pair[0].split(",")
    x2, y2 = point_pair[1].split(",")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    #slope = (y1 - y2)/(x1 - x2)
    #intercept = (x1*y2 - x2*y1)/(x1-x2)