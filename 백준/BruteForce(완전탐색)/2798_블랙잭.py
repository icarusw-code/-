from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for card in combinations(cards, 3):
    if sum(card) <= m:
        if sum(card) >= answer:
            answer = sum(card)

print(answer)
