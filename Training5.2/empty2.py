from itertools import chain

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


seq = list(chain(*rows))
max1 = max(seq)
first_max = [max1, int(seq.index(max1) // c), seq.index(max1) % c]
# print(first_max)

#try to block the row
copy_row = rows[first_max[1]]
rows[first_max[1]] = [0] * c
seq = list(chain(*rows))
max2 = max(seq)
second_max = [max2, int(seq.index(max2) // c), seq.index(max2) % c]
rows[first_max[1]] = copy_row
# print('max2', max2)

#try to block the column
copy_column = []
for ind_out, el in enumerate(rows):
    for ind_in, elem in enumerate(el):
        if ind_in == first_max[2]:
            copy_column.append(elem)
            rows[ind_out][ind_in] = 0

seq = list(chain(*rows))
max22 = max(seq)
second_second_max = [max22, int(seq.index(max22) // c), seq.index(max22) % c]
# print('max22', max22)


if max22 < max2:
    ans.append(str(second_second_max[1] + 1))
    ans.append(str(first_max[2] + 1))
    print(' '.join(ans))
elif max22 > max2:
    ans.append(str(first_max[1] + 1))
    ans.append(str(second_max[2] + 1))
    print(' '.join(ans))
else:
    # take a look if fmax[2] = 0 and smax[1] = 0 max22 is the least
    copy_row = rows[second_max[1]]
    rows[second_max[1]] = [0] * c
    seq = list(chain(*rows))
    max3_1 = max(seq)
    rows[second_max[1]] = copy_row
    for ind_out, el in enumerate(rows):
        for ind_in, elem in enumerate(el):
            if ind_in == first_max[2]:
                rows[ind_out][ind_in] = copy_column[ind_out]

    # take a look if fmax[1] = 0 and smax[2] = 0 max2 is the least
    copy_row = rows[first_max[1]]
    rows[first_max[1]] = [0] * c
    copy_column = []
    for ind_out, el in enumerate(rows):
        for ind_in, elem in enumerate(el):
            if ind_in == second_max[2]:
                copy_column.append(elem)
                rows[ind_out][ind_in] = 0
    seq = list(chain(*rows))
    max3_2 = max(seq)
    # print(max3_1, max3_2)

    # The solution
    if max3_2 < max3_1:
        ans.append(str(first_max[1] + 1))
        ans.append(str(second_max[2] + 1))
        print(' '.join(ans))
    elif max3_2 > max3_1:
        ans.append(str(second_max[1] + 1))
        ans.append(str(first_max[2] + 1))
        print(' '.join(ans))

