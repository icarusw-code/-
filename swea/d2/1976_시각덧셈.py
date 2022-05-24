import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    if m1 + m2 >= 60:
        m = (m1+m2) - 60
        h += 1
    else:
        m = m1 + m2
    if h >= 12:
        h -= 12

    print(f"#{tc} {h} {m}")
