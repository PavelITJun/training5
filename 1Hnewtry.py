from decimal import Decimal

data = list(map(Decimal, input().split()))
L = data[0]
ans = 0
if min(data[1], data[3]) == data[1]:
    x1 = data[1]
    v1 = data[2]
    x2 = data[3]
    v2 = data[4]
else:
    x1 = data[3]
    v1 = data[4]
    x2 = data[1]
    v2 = data[2]


def sol():
    global L, ans, x1, v1, x2, v2
    if v1 > 0 and v2 > 0:
        if x1 <= L - x2:
            ans = (x2 - x1) / (v1 + v2)
            return ans
        elif x1 > L - x2:
            ans += (L - x2) / v2
            x1 += (L - x2) * v1 / v2
            x2 = 0

        if x1 <= L / 2 and x2 <= L / 2 and x1 > x2:
            if (L / 2 - x1) / v1 >= (L / 2 - x2) / v2:
                ans += (x1 - x2) / (v2 - v1)
                return ans
            elif L / (2 * v1) < L / (2 * v2):
                ans += (L / 2 - x1) / v1
                x2 += (L / 2 - x1) * v2 / v1
                x1 = L / 2
                ans += (x1 - x2) / (v1 + v2)
                return ans

        if x1 <= L / 2 and x2 <= L / 2 and x1 < x2:
            if (L / 2 - x2) / v2 >= (L / 2 - x1) / v1:
                ans += (x2 - x1) / (v1 - v2)
                return ans
            elif (L / 2 - x2) / v2 < (L / 2 - x1) / v1:
                ans += (L / 2 - x2) / v2
                x2 += (L / 2 - x1) * v1 / v2
                x1 = L / 2
                ans += (x2 - x1) / (v1 + v2)
                return ans

        if x1 >= L / 2 and x2 >= L / 2:
            if (L - x2) / v2 >= (L - x1) / v1:
                ans += (x2 - x1) / (v1 - v2)
                return ans
            elif (L - x2) / v2 < (L - x1) / v1:
                ans += (L - x2) / v2
                x1 += (L - x2) / v2 * v1
                x2 = 0
                ans += (L - x1) * v2 / (v1 + v2)
                return ans

print(sol())