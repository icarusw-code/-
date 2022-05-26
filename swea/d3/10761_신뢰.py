t = int(input())

for tc in range(1, t+1):

    arr = list(map(str, input().split()))

    bp, op = 1, 1
    bw, ow = 0, 0

    answer = 0

    for i in range(1, len(arr), 2):
        who, number = arr[i], int(arr[i+1])

        if who == "B":
            tmp = max(0, abs(number - bp) - bw) + 1
            bp = number
            bw = 0
            answer += tmp
            ow += tmp
        else:
            tmp = max(0, abs(number - op) - ow) + 1
            op = number
            ow = 0
            answer += tmp
            bw += tmp

    print(f"#{tc} {answer}")
