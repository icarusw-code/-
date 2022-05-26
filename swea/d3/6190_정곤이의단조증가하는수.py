from itertools import combinations
import sys
sys.stdin = open("input.txt")

t = int(input())

def check(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            return False
    return True

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = []
    for i in combinations(arr, 2):
        a, b = i
        if check(a*b):
            answer.append(a*b)

    if len(answer) == 0:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {max(answer)}")