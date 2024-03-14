from itertools import chain #Not bad try, but 9 test suck dick

rc = list(map(int, input().split()))
r = rc[0]
c = rc[1]
rows = []
columns = []
ans = []
for _ in range(r):
    a = list(map(int, input().split()))
    rows.append(a)
for el in range(c):
    a = []
    for elem in rows:
        a.append(elem[el])
    columns.append(a)


def find_max2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max2


seq = list(chain(*rows))
max1 = max(list(chain(*rows)))
max2 = find_max2(list(chain(*rows)))
# print(seq)
first_max = [max1, int(seq.index(max1) // c), seq.index(max1) % c]
second_max = [max2, int(seq.index(max2) // c), seq.index(max2) % c]
# print(first_max, second_max, '-------', sep='\n')
if first_max[1] == second_max[1]:
    ans.append(str(first_max[1] + 1))
    rows.pop(first_max[1])
    seq = list(chain(*rows))
    max3 = max(seq)
    if first_max[1] - 1 < seq.index(max3) // c:
        third_max = [max3, (seq.index(max3) // c + 1), seq.index(max3) % c]
    else:
        third_max = [max3, seq.index(max3) // c, seq.index(max3) % c]
    ans.append(str(third_max[2] + 1))
    print(' '.join(ans))
elif first_max[2] == second_max[2]:
    columns.pop(first_max[2])
    seq = list(chain(*columns))
    max3 = max(seq)
    if first_max[2] - 1 < seq.index(max3) // r:
        third_max = [max3, seq.index(max3) % r, (seq.index(max3) // r) + 1]
    else:
        third_max = [max3, seq.index(max3) % r, seq.index(max3) // r]
    ans.append(str(third_max[1] + 1))
    ans.append(str(first_max[2] + 1))
    print(' '.join(ans))
else:
    rows[first_max[1]][first_max[2]] = 0
    rows[second_max[1]][second_max[2]] = 0
    seq = list(chain(*rows))
    max3 = max(seq)
    third_max = [max3, seq.index(max3) // c, seq.index(max3) % c]
    if third_max[1] == first_max[1]:
        ans.append(str(third_max[1] + 1))
        ans.append(str(second_max[2] + 1))
        print(' '.join(ans))
    elif third_max[1] == second_max[1]:
        ans.append(str(third_max[1] + 1))
        ans.append(str(first_max[2] + 1))
        print(' '.join(ans))
    elif third_max[2] == first_max[2]:
        ans.append(str(second_max[1] + 1))
        ans.append(str(third_max[2] + 1))
        print(' '.join(ans))
    elif third_max[2] == second_max[2]:
        ans.append(str(first_max[1] + 1))
        ans.append(str(third_max[2] + 1))
        print(' '.join(ans))
    else:
        ans.append(str(first_max[1] + 1))
        ans.append(str(second_max[2] + 1))
        print(' '.join(ans))