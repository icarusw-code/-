import sys
sys.stdin = open("input.txt")

t = int(input())

def check(n):
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

for tc in range(1, t+1):
    n = int(input())
    answer = 0
    p = []
    for i in range(2, n):
        if check(i):
            p.append(i)

    for i in range(len(p)):
        for j in range(i, len(p)):
            for k in range(j, len(p)):
                if p[i]+p[j]+p[k] == n:
                    answer += 1
    print(f"#{tc} {answer}")