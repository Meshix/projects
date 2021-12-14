# Count Bit Significance
ones = [0] * 12
zeros = [0] * 12
with open ("2021/D3/input.txt", "r") as f:
    for line in f:
        for i, c in enumerate(line.strip()):
            if c == "1":
                ones[i] += 1
            else:
                zeros[i] += 1
res =""

# Part 1 Ouptut
for i in range(12):
    res += "1" if ones[i] >= zeros[i] else "0"
print(int(res, 2) * int(''.join('1' if x == '0' else '0' for x in res), 2))

# Part 2
lines = []
with open("2021/D3/input.txt", "r") as f:
    for line in f:
        lines.append(list(line.strip()))

tempO = lines
tempC = lines
for i in range(12):
    newTempO = []
    newTempC = []
    columnO = [row[i] for row in tempO]
    columnC = [row[i] for row in tempC]
    bitO = '1' if columnO.count('1') >= columnO.count('0') else '0'
    bitC = '0' if columnC.count('0') <= columnC.count('1') else '1'
    for j in range(len(tempO)):
        if tempO[j][i] == bitO:
            newTempO.append(tempO[j])
    tempO = newTempO
    for j in range(len(tempC)):
        if tempC[j][i] == bitC:
            newTempC.append(tempC[j])
    if len(tempC) > 1:
        tempC = newTempC
print(int(''.join(tempO[0]), 2) * int(''.join(tempC[0]), 2))