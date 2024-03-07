# Создаем шахматную доску
board = []
for _ in range(8):
    row = input().strip()
    board.append(row)

column_board = []
for i in range(8):
    column = ''
    for j in range(8):
        column += board[j][i]
    column_board.append(column)

# Функция для проверки, бьет ли ладья заданную клетку
def check_rook(x, y):
    if y < 7:
        lis = board[x][(y + 1):]
        for ind, el in enumerate(lis):  # right hor
            if lis[ind] == 'B':
                break
            if lis[ind] == 'R':
                board[x] = board[x][:y] + "1" + board[x][(y + 1):]
                return

    if y > 0:
        lis = board[x][(y - 1)::-1]
        for ind, el in enumerate(lis):  # left hor
            if lis[ind] == 'B':
                break
            if lis[ind] == 'R':
                board[x] = board[x][:y] + "1" + board[x][(y + 1):]
                return

    if x < 7:
        lis = column_board[y][(x + 1):]
        for ind, el in enumerate(lis):  # down vert
            if lis[ind] == 'B':
                break
            if lis[ind] == 'R':
                board[x] = board[x][:y] + "1" + board[x][(y + 1):]
                return

    if x > 0:
        lis = column_board[y][(x - 1)::-1]
        for ind, el in enumerate(lis):  # up vert
            if lis[ind] == 'B':
                break
            if lis[ind] == 'R':
                board[x] = board[x][:y] + "1" + board[x][(y + 1):]
                return

# Функция для проверки, бьет ли слон заданную клетку
def check_bishop(x, y):
    hor, vert = x, y # right down
    while True:
        hor += 1
        vert += 1
        if hor > 7 or vert > 7:
            break
        if board[hor][vert] == 'R':
            break
        if board[hor][vert] == 'B':
            board[x] = board[x][:y] + '1' + board[x][(y+1):]
            return

    hor, vert = x, y #right up
    while True:
        hor -= 1
        vert += 1
        if hor < 0 or vert > 7:
            break
        if board[hor][vert] == 'R':
            break
        if board[hor][vert] == 'B':
            board[x] = board[x][:y] + '1' + board[x][(y + 1):]
            return

    hor, vert = x, y  # left down
    while True:
        hor += 1
        vert -= 1
        if hor >= 8 or vert < 0:
            break
        if board[hor][vert] == 'R':
            break
        if board[hor][vert] == 'B':
            board[x] = board[x][:y] + '1' + board[x][(y + 1):]
            return

    hor, vert = x, y  # left up
    while True:
        hor -= 1
        vert -= 1
        if hor < 0 or vert < 0:
            break
        if board[hor][vert] == 'R':
            break
        if board[hor][vert] == 'B':
            board[x] = board[x][:y] + '1' + board[x][(y + 1):]
            return

# Проходим по всем клеткам и проверяем, не бьется ли клетка ни ладьей, ни слоном
empty_cells = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            check_rook(i, j)
            check_bishop(i, j)

for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            empty_cells += 1

print(empty_cells)
for row in board:
    print(row)