n, c = map(int, input().split())
m = int(input())
arr = list(list(map(int, input().split())) for _ in range(m))
arr.sort(key = lambda x: (x[1], x[0]))

answer = 0
con = [0] + [c] * (n)

for start, end, capacity in arr:
    tmp = min(min(con[start:end]), capacity)
    for i in range(start, end):
        con[i] -= tmp
    answer += tmp

print(answer)