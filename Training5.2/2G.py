t = int(input()) #TL


def sol(n, data):
    now_list = []
    ans_list = []
    ind = 0
    now_min = 10**5 + 1

    while ind < len(data):
        now_min = min(now_min, data[ind])
        now_list.append(data[ind])
        if now_min >= len(now_list):
            ind += 1
        else:
            now_list.pop()
            ans_list.append(str(len(now_list)))
            now_list = []
            now_min = 10**5 + 1
    if now_list:
        ans_list.append(str(len(now_list)))

    print(len(ans_list))
    print(' '.join(ans_list))


for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    sol(n, data)
