import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    stone = [abs(i) for i in arr]

    print(f"#{tc} {min(stone)} {stone.count(min(stone))}")

