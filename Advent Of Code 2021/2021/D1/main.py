with open('inputs.txt') as f:
    lines = f.read().split("\n")

integer_map = map(int, lines)
integer_list = list(integer_map)
increasings1 = 0
increasings2 = 0

for i in range(len(integer_list)-3):
    if integer_list[i+1] > integer_list[i]:
        increasings1 += 1
    if integer_list[i+3] > integer_list[i]:
        increasings2 += 1
print(increasings2)