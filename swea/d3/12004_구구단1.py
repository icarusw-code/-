import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    answer = "No"

    for i in range(1,10):
        if n % i == 0 and n // i <= 9:
            answer = "Yes"
            break

    print(f"#{tc} {answer}")
