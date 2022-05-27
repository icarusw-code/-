import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    student = list(i for i in range(1, n+1))

    for i in arr:
        student.remove(i)

    print(f"#{tc}", end=" ")
    print(*student)