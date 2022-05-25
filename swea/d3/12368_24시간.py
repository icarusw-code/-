import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())

    if a + b < 24:
        print(f"#{tc} {a + b}")
    else:
        print(f"#{tc} {a + b -24}")

