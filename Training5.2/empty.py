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
for index, el in enumerate(sorted_power):
    if el[0] <= 0 or index == len(sorted_power) - 1:
        indexes_last = []
        for elem in sorted_power[index:]:
            indexes_last.append(elem[1])
        values_last = []
        for index_last in indexes_last:
            values_last.append(data[index_last][0])
        appendant = max(values_last)
        height += appendant
        for dev in data:
            if dev[0] == appendant:
                help_ind = data.index(dev)
        if str(help_ind + 1) not in indexes:
            indexes.append(str(help_ind + 1))
        for numb in range(1, N + 1):
            if str(numb) not in indexes:
                indexes.append(str(numb))
        break
    height += el[0]
    indexes.append(str(el[1] + 1))
print(height)
print(' '.join(indexes))