import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr) / n
    arr.sort()

    answer = 0
    for i in arr:
        if i <= avg:
            answer += 1

    print(f"#{tc} {answer}")