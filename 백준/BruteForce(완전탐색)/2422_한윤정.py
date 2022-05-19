from itertools import combinations

n, m = map(int, input().split())

nos = list(list(map(int, input().split())) for _ in range(m))

answer = set()
for ice in combinations(range(1,n+1), 3):
    ice = list(ice)
    for no in nos:
        if no not in ice:
            print(no)
            print(ice)

# print(answer)