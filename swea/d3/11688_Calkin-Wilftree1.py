import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    word = input()
    arr = [i for i in word]
    now = [1, 1]

    for i in arr:
        if i == "L":
            now[0] = now[0]
            now[1] = now[0] + now[1]
        else:
            now[0] = now[0] + now[1]
            now[1] = now[1]

    print(f"#{tc}", end=" ")
    print(*now)

