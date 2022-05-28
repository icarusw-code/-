import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())

    if a > 9 or b > 9:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {a*b}")