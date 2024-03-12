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
    global L, x1, x2, v1, v2, ans
    if x1 == L-x2: #the easiest part
        return 0

    if v1 < 0 and v2 < 0:
        x1 = L - x1
        x2 = L - x2
        x1, x2 = x2, x1
        v1 = abs(v1)
        v2 = abs(v2)
        v1, v2 = v2, v1

    if v1 > 0 and v2 > 0:
        if x1 < L/2 <= x2 and L-x2 > x1: #case 1
            ans += (x2-x1)/(v1+v2)
            return ans


        if x1 < L/2 and x2 > L/2 and L-x2 < x1: #case 2
            ans += (L/2-x1)/v1
            x2 += (L/2-x1) * v2 / v1
            x2 %= L
            x1 = L/2
            if x2 > L/2: #case 2.1
                if (L-x2)/v2 >= (L-x1)/v1:
                    ans += (x2-x1)/(v1-v2)
                    return ans
                else:
                    ans += (L-x2)/v2
                    x1 += (L-x2)*v1/v2
                    x2 = 0
                    ans += (L-x1)/(v1+v2)
                    return ans
            else: #case 2.2
                ans += (x1-x2)/(v1+v2)
                return ans

        if x1 < x2 < L/2: #case 4
            if (L/2 - x2)/v2 >= (L/2 - x1)/v1:
                ans += (x2-x1)/(v1-v2)
                return ans
            else:
                ans += (L/2 - x2)/v2
                x1 += (L/2 - x2)*v1/v2
                x2 = L/2
                ans += (x2-x1)/(v1+v2)
                return ans

        if L/2 < x1 < x2: #case 5
            if (L-x2)/v2 >= (L-x1)/v1:
                ans += (x2-x1)/(v1-v2)
                return ans
            else:
                ans += (L-x2)/v2
                x1 += (L-x2)*v1/v2
                x2 = 0
                ans += (x2-x1)/(v1+v2)
                return ans

    if v1 > 0 > v2:
        

    return ans


print(sol())
