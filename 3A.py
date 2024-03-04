n = int(input())


def sol(n):
    ans = 0
    for _ in range(n):
        el = int(input())
        if el % 4 == 0:
            ans += el // 4
        elif el % 4 == 1:
            ans += el // 4 + 1
        else:
            ans += el // 4 + 2
    return ans


print(sol(n))