import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    m, d = map(int, input().split())

    day = [3,4,5,6,0,1,2]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print(f"#{tc} {day[(sum(mon[:m-1]) + d) % 7]}")

