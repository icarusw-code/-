import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    D, L, N = map(int, input().split())
    now = 0
    answer = 0

    while now < N:
        answer += D*(1 + now*L*0.01)
        now += 1

    print(f"#{tc} {int(answer)}")



