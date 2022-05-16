n = int(input())
drink = list(map(int, input().split()))

drink.sort(reverse=True)
answer = drink[0]

for i in range(1, n):
    answer += (drink[i] / 2)

print("%g"%answer)
