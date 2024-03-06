x = int(input())
y = int(input())
p = int(input())
warriors = 0
attackers = 0
count = 0
while True:
    count += 1
    if warriors > 0: #first step
        if warriors < x:
            attackers = x - warriors
            warriors = 0
            y -= attackers
            if y <= 0:
                print('The building are fallen')
                break
        else:
            warriors -= x
            x = 0
            print('All my warriors are dead')
            break
    else:
        y -= x
        if y <= 0:
            print('The building are fallen')
            break

    x -= warriors #second step
    warriors += p #third step

print(count)