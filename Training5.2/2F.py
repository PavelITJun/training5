secs = int(input())
wheel = list(map(int, input().split()))
abk = list(map(int, input().split()))
a, b, k = abk
prize_list = []
ind = 0

while a > k: #right side
    a -= k
    ind += 1
prize = wheel[ind % secs]
prize_list.append(prize)
for i in range((b-a)//k):
    prize = wheel[(ind + i + 1) % secs]
    prize_list.append(prize)

print(prize_list)