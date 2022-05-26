import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(list(map(float, input().split())) for _ in range(n))

    answer = 0
    for p, x in arr:
        answer += p * x

    print(f"#{tc} {answer}")
