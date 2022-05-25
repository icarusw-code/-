import sys
sys.stdin = open("input.txt")

t = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    d = d2 - d1
    m = m2 - m1
    answer = d + 1
    for i in range(m):
        answer += month[m1+i]
    print(f"#{tc} {answer}")