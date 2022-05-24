import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(list(map(str, input().split())) for _ in range(n))
    arr2 = [[arr[i][j] for i in range(n)] for j in range(n)]
    answer = 0

    for row in arr:
        line = "".join(row).split("0")
        answer += line.count("1"*k)

    for row in arr2:
        line = "".join(row).split("0")
        answer += line.count("1"*k)

    print(f"#{tc} {answer}")
