n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 0
m = cost[0]

for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    answer += m * distance[i]

print(answer)
