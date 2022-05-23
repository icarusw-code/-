import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    n_max = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] >= n_max:
            n_max = arr[i]
        else:
            answer += (n_max - arr[i])
    print(f"#{tc} {answer}")




