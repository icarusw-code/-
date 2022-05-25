import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    answer =""
    for _ in range(1, n+1):
        word, count = input().split()
        answer += word*(int(count))

    print(f"#{tc}")
    for i in range(0, len(answer), 10):
        print(answer[i: i + 10])
