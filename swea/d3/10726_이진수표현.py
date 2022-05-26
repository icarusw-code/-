import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):

    n, m = map(int, input().split())
    new_m = bin(m)[2:]
    answer = "ON"

    if len(new_m) < n:
        answer = "OFF"

    for i in str(new_m[len(new_m)-n:]):
        if i == "0":
            answer = "OFF"

    print(f"#{tc} {answer}")