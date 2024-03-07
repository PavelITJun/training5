nkd = list(map(int, input().split()))
n, k, d = nkd[0], nkd[1], nkd[2]

flag = False
for numb in range(10):
    if (n * 10 + numb) % k == 0:
        flag = True
        n = n * 10 + numb
        print(str(n) + ('0' * (d - 1)))
        break

if not flag:
    print(-1)