import sys
sys.stdin = open("input.txt")


def check(x, y):
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(4):
        count = 0
        nx, ny = x, y
        while 0<= nx < n and 0<= ny < n and board[nx][ny] == "o":
            count += 1
            nx += dx[i]
            ny += dy[i]

        if count >= 5:
            return True
    return False

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = list(input() for _ in range(n))
    result = "NO"

    for i in range(n):
        for j in range(n):
            if check(i, j):
                result = "YES"
                break

        if result == "YES":
            break

    print(f"#{tc} {result}")


