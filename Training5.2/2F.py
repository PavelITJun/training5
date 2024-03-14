secs = int(input())
wheel = list(map(int, input().split()))
left_wheel = [wheel[0]]
left_wheel.extend(wheel[-1:0:-1])
abk = list(map(int, input().split()))
a, b, k = abk
prizes_list = []
min1 = min(a//k//secs, b//k//secs)
a -= 0.1
b -= 0.1
a = int(a//k)
b = int(b//k)
a -= (min1 * secs)
b -= (min1 * secs)
rinds = []
linds = []
if b == secs:
    rinds.extend([x for x in range(a, secs)])
elif b > secs:
    rinds.extend([x for x in range(a, secs)])
    b -= secs
    if b >= secs:
        rinds = [x for x in range(secs)]
    else:
        rinds.extend([x for x in range(0, b+1)])
else:
    rinds.extend([x for x in range(a, b + 1)])
for ind in set(rinds):
    prizes_list.append(wheel[ind])
    prizes_list.append(left_wheel[ind])
print(max(prizes_list))
