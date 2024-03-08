NK = tuple(map(int, input().split()))
N, K = NK[0], NK[1]
prices = list(map(int, input().split()))
ans = 0

for ind, price in enumerate(prices):
    now_prices = prices[ind:(K + ind + 1)]
    now_max = max(now_prices)
    now_max_ind_list = []
    for index, el in enumerate(now_prices):
        if el == now_max:
            now_max_ind_list.append(index)
    if now_prices[:now_max_ind_list[-1]]:
        now_min = min(now_prices[:now_max_ind_list[-1]])
        now_ans = now_max - now_min
        if now_ans > ans:
            ans = now_ans
    if K + ind + 1 == N:
        break
    else:
        continue


print(ans)
