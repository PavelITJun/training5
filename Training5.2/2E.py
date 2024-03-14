N = int(input()) #snail
data = []
height = 0
indexes = []
for _ in range(N):
    data.append(list(map(int, input().split())))
power = []
for ind, el in enumerate(data):
    power.append([el[0] - el[1], ind])
sorted_power = sorted(power, key=lambda x: x[0], reverse=True)
print(data)
print(sorted_power)