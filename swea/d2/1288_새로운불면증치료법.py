import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    answer = -1
    check = set(list(i for i in range(10)))
    sheep = set()

    while True:
        m = n
        answer += 1
        m *= (answer+1)
        if sheep == check:
            break

        for i in str(m):
            sheep.add(int(i))

    print(f"#{tc} {answer*n}")
