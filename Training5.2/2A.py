n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
x_list = []
y_list = []
max_x, max_y = -10**9 - 1, -10**9 - 1
min_x, min_y = 10**9 + 1, 10**9 + 1
for el in data:
    if el[0] < min_x:
        min_x = el[0]
    if el[0] > max_x:
        max_x = el[0]
    if el[1] < min_y:
        min_y = el[1]
    if el[1] > max_y:
        max_y = el[1]

print(min_x, min_y, max_x, max_y, sep=' ')