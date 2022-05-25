import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    check = True

    if c == 100 and b != 100:
        answer = "Broken"
    elif c == 0 and b != 0:
        answer = "Broken"
    else:
        for i in range(1, a+1):
            if i*b/100 == i*b //100:
                answer = "Possible"
                check = False
                break
        if check:
            answer = "Broken"

    print(f"#{tc} {answer}")