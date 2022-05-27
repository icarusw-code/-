import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, q = map(int, input().split())

    answer = [0] * n

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            answer[j] = i

    print(f"#{tc}", end=" ")
    print(*answer)


