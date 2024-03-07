n = int(input())
numbers = list(map(str, input().split()))
ans = ''


def rec(numbers, hist='', index=0):
    global ans
    if index == len(numbers) - 1:
        hist += numbers[-1]
        if eval(hist) % 2 == 1:
            ans = hist
        return
    hist += numbers[index] + '+'
    rec(numbers, hist, (index+1))
    hist = hist[:-1]
    hist += '*'
    rec(numbers, hist, (index+1))


rec(numbers)
sol = ''
for el in ans:
    if el == '*':
        sol += 'x'
    elif el == '+':
        sol += '+'

print(sol)