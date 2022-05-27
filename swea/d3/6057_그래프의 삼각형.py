t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [[] for _ in range(n+1)]

    for i in range(m):
        s, e = map(int, input().split())
        board[s].append(e)
        board[e].append(s)
    answer = 0

    for i in range(n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if (i in board[j]) and (j in board[k]) and (k in board[i]):
                    answer += 1

    print(f"#{tc} {answer}")