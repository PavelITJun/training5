whc = list(map(int, input().split()))
w, h, c = whc
lines = []
while True:
    line = str(input())
    print(line)
    if '\n' in line:
        lines.append(line)
    else:
        break
