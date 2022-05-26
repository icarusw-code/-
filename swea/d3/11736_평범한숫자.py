t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(1, n-1):
        if arr[i] != max(arr[i-1:i+2]) and arr[i] != min(arr[i-1:i+2]):
            answer += 1

    print(f"#{tc} {answer}")