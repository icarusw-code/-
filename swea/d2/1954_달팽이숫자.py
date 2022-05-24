t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]

    # 우,하,좌,상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    cnt, flag = 1, 0
    x, y = 0, 0
    while cnt <= n**2:
        board[y][x] = cnt
        cnt += 1
        nx = x + dx[flag]
        ny = y + dy[flag]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[ny][nx]:
            flag = (flag+1) % 4

        x += dx[flag]
        y += dy[flag]

    print(f"#{tc}")
    for i in range(n):
        print(" ".join(map(str, board[i])))
