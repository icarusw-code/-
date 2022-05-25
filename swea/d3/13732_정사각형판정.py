from collections import deque
import sys
sys.stdin = open("input.txt")

t = int(input())

def bfs(squre, board):
    len_sq = len(square) ** (0.5)
    if len_sq % 1 != 0:
        return "no"
    x, y = squre.popleft()
    for i in range(x, x+int(len_sq)):
        for j in range(y, y+int(len_sq)):
            if board[i][j] != "#":
                return "no"
    return "yes"


for tc in range(1, t+1):
    n = int(input())
    board = list((input()) for _ in range(n))

    square = deque((i,j) for i in range(n) for j in range(n) if board[i][j] == "#")
    answer = bfs(square, board)
    print(f"#{tc} {answer}")