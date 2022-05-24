import sys
sys.stdin = open("input.txt")

t = int(input())
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, t+1):
    n = int(input())
    answer = [0] * len(coins)

    for idx, coin in enumerate(coins):
        if n == 0:
            break
        answer[idx] = (n // coin)
        n -= (n // coin) * coin
    print(f"#{tc}")
    print(*answer)