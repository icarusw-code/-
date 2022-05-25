t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = int(1e9)

    for i in range(7):
        if arr[i] == 1:
            idx = i
            tmp = n
            cnt = 0
            while tmp:
                if arr[idx] == 1:
                    tmp -= 1
                cnt += 1
                idx = (idx + 1) % 7

            if answer > cnt:
                answer = cnt

    print(f"#{tc} {answer}")
