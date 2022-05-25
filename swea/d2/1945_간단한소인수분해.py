import sys
sys.stdin = open("input.txt")

t = int(input())
arr = [2, 3, 5, 7, 11]
for tc in range(1, t+1):
    n = int(input())
    answer = []
    for i in arr:
        tmp = 0
        while n % i == 0:
            tmp += 1
            n = n // i
        answer.append(tmp)
    print(f"#{tc}", end=" ")
    print(*answer)