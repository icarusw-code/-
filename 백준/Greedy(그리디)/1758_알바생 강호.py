n = int(input())
cost = list(int(input()) for _ in range(n))

cost.sort(reverse=True)
answer = 0
for i in range(n):
    if cost[i] - i < 0:
        continue
    else:
        answer += (cost[i] - i)

print(answer)