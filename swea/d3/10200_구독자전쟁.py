import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n, a, b= map(int, input().split())

    if a >= b:
        min_value = b
    else:
        min_value = a

    if (a+b) - n >= 0:
        max_value = (a+b) -n
    else:
        max_value = 0

    print(f"#{tc} {min_value} {max_value}")