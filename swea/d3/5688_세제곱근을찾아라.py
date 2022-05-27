import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    if (round(n**(1/3), 2)).is_integer():
        answer = int(round(n ** (1/3), 2))
        print(f"#{tc} {answer}")
    else:
        print(f"#{tc} -1")
