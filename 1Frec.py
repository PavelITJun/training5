n = int(input())
numbers = list(map(str, input().split()))
ans = ''


def sol(values, string='', index=0):
    global ans
    string = string + values[index]
    if index == len(values) - 1:
        if eval(string) % 2 == 1:
            ans = ''
            for el in string:
                if el == '+':
                    ans += '+'
                elif el == '*':
                    ans += 'x'
            return ans
        return ''
    sol(values, string+'*', index+1)
    sol(values, string+'+', index+1)
    return ans



print(sol(numbers))
