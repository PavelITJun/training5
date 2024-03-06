from decimal import Decimal

data = list(map(Decimal, input().split()))
L, x1, v1, x2, v2 = data[0], data[1], data[2], data[3], data[4]
const = Decimal("0.0000000001")
count = 0
