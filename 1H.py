from decimal import Decimal

data = list(map(Decimal, input().split()))
L, x1, v1, x2, v2 = data[0], data[1], data[2], data[3], data[4]
const = Decimal("0.01")
count = 0
while True:
    if min(abs(x1-L), x1) == min(abs(x2-L), x2):
        print('YES', count*const, sep='\n')
        break

    count += 1
    x1 += (v1 * const)
    if x1 >= L:
        x1 -= L

    x2 += (v2 * const)
    if x2 >= L:
        x2 -= L