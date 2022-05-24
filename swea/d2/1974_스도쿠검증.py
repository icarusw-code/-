import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    board = list(list(map(int, input().split())) for _ in range(9))
    board2 = list(list(board[i][j] for i in range(9)) for j in range(9))
    answer = 1

    for i in board:
        if len(i) != len(set(i)):
            answer = 0
            break

    for j in board2:
        if len(j) != len(set(j)):
            answer = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for p in range(3):
                for q in range(3):
                    tmp.append(board[i+p][j+q])
            if len(tmp) != len(set(tmp)):
                answer = 0
                break

    print(f"#{tc} {answer}")
