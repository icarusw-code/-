import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    arr = list(input())
    now = arr.count("o")
    left = 15 - len(arr)
    if now + left >= 8:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")


