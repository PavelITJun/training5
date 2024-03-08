N = int(input())
ropes = list(map(int, input().split()))
if 2 * max(ropes) > sum(ropes):
    print(2 * max(ropes) - sum(ropes))
else:
    print(sum(ropes))