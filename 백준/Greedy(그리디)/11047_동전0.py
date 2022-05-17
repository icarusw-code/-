n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
answer = 0

for coin in coins:
    if k < 0:
        break
    if k // coin > 0:
        answer += k // coin
        k -= (k // coin) * coin

print(answer)