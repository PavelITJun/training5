n = int(input())
numbers = list(map(int, input().split()))
first_num = 0
count_odd = 0
count_oven = 0
ans = []
count = -1


def sol(numbers):  # если первое число нечетное
    global count_odd, count_oven

    for num in numbers[1:]:
        if num % 2 == 1:
            count_odd += 1
        else:
            count_oven += 1

    if count_oven > 0:
        ans.append('+')
        ans.append('*' * (len(numbers) - 2))
    else:
        if count_odd % 2 == 0:
            ans.append('+' * (len(numbers) - 1))
        else:
            ans.append('*' * (len(numbers) - 1))

    print(''.join(ans).replace('*', 'x'))
    return


if numbers[0] % 2 == 1:
    sol(numbers)
else:
    for num in numbers:
        first_num += num
        count += 1
        if abs(first_num % 2) == 1:
            ans.append('+' * count)
            num_copy = numbers
            numbers = []
            numbers.append(first_num)
            numbers.extend(num_copy[(count + 1):])
            if len(numbers) > 1:
                sol(numbers)
                break
            else:
                print('+' * (len(num_copy) - 1))
                break
