import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, d = map(int, input().split())
    answer = 0

    while True:
        if (2*d+1)*answer >= n:
            break
        else:
            answer += 1

    print(f"#{tc} {answer}")
