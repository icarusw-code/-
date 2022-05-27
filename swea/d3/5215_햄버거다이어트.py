from itertools import combinations
import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, L = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))

    answer = 0

    for i in range(1, n+1):
        for j in combinations(arr, i):
            value = 0
            cal = 0
            for i in j:
                value += i[0]
                cal += i[1]
            if cal > L:
                continue
            if answer < value:
                answer = value

    print(f"#{tc} {answer}")