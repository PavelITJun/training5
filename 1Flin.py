n = int(input())
numbers = list(map(int, input().split()))
ans = ''

for ind, el in enumerate(numbers):
    if el % 2 == 1:
        if ind == 0:
            ans += '+'
        elif ind + 1 == len(numbers):
            ans = ans[:-1] + '+'
        continue
    else:
        ans += 'x'
print(ans)
