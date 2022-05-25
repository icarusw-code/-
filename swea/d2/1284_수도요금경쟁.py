import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    A, B = 0, 0

    A = p * w

    if w <= r:
        B = q
    else:
        B = q + (w-r)*s

    print(f"#{tc} {min(A, B)}")