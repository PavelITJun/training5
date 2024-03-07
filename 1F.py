from itertools import product
n = int(input())
numbers = list(map(str, input().split()))
signs = product(['+', '*'], repeat=len(numbers)-1)
found = False
ans = ''
for el in signs:
    exp = [numbers[0]]
    for _ in range(n - 1):
        exp.append(el[_])
        exp.append(numbers[_ + 1])
    exp = ''.join(exp)
    if eval(exp) % 2 == 1:
        ans = exp
        found = True
        break
    if found:
        break

sol = ''
for el in ans:
    if el == '*':
        sol += 'x'
    elif el == '+':
        sol += '+'

print(sol)