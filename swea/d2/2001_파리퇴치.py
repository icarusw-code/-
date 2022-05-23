import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))
    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for p in range(i, i+m):
                for q in range(j, j+m):
                    total += arr[p][q]
            if answer < total:
                answer = total

    print(f"#{tc} {answer}")
