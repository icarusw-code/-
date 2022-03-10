# 순열
n = int(input())

arr = list(map(int, input().split()))

result = [0] * n

used = [0] * len(arr)

def per(lev):
    if lev == n:
        print(*result)
        return

    for i in range(len(arr)):
        if used[i] == 1:
            continue
        used[i] = 1
        result[lev] = arr[i]
        per(lev + 1)
        used[i] = 0

per(0)