lines = []
Rpos = []
Bpos = []
false_ans = 0
for _ in range(8): #collecting data
    el = str(input())
    for ind, elem in enumerate(el):
        if elem == 'R':
            Rpos.append((_, ind))
        elif elem == 'B':
            Bpos.append((_, ind))
    lines.append(el)

for R in Rpos:
    line = lines[R[0]]

    count = 0
    for cell in line[R[1]+1:]: #right side
        if cell == '0':
            continue
        if cell == '*':
            count += 1
        else:
            break
        lines[R[0]] = line[:R[1] + 1] + '0' * count + line[:8 - len(line[:R[1] + 1]) - count]

    count = 0
    help_list = line[:R[1]+1]
    for cell in reversed(help_list):  # left side
        if cell == '0':
            continue
        if cell == '*':
            count += 1
        else:
            break
        lines[R[0]] =


print(lines)