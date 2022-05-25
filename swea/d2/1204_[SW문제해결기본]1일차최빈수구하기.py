import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    score = list(map(int, input().split()))
    tmp = 0
    answer = 0
    for i in range(101):
        if tmp <= score.count(i):
            tmp = score.count(i)
            answer = i
    print(f"#{n} {answer}")
