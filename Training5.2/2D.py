n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

count = 0

for el in data:
    x, y = el[0], el[1]
    if (x+1, y) not in data:
        count += 1
    if (x-1, y) not in data:
        count += 1
    if (x, y+1) not in data:
        count += 1
    if (x, y-1) not in data:
        count += 1

print(count)