import sys
sys.stdin = open("input.txt")

t = int(input())

def check(n):
    arr = list(int(i) for i in str(n))
    if arr == arr[::-1]:
        return True
    else:
        return False

for tc in range(1, t+1):
    a, b = map(int, input().split())
    answer = 0
    for i in range(a, b+1):
        if (i**0.5).is_integer():
            # print(i)
            if check(i) and check(int(i**0.5)):
                answer += 1
    print(f"#{tc} {answer}")