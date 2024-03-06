nkd = list(map(int, input().split()))
n, k, d = nkd[0], nkd[1], nkd[2]


def get_numb(n):
    global k
    for numb in range(10):
        if int(str(n) + str(numb)) % k == 0:
            return int(str(n) + str(numb))
    return -1


def answer_list(n, k, d):
    answers = []
    for _ in range(d):
        cur_ans = get_numb(n)
        if cur_ans == -1:
            return -1
        answers.append(cur_ans)
        n //= k
    return answers


def sol(n, k, d):
    ans_list = answer_list(n, k, d)
    if ans_list == -1:
        return -1
    for el in ans_list[::-1]:
        if el != 0:
            return el


print(sol(n, k, d))