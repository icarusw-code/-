from time import time


n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key= lambda x:(x[1], x[0]))

answer = 0
last = 0

for time in times:
    start, end = time
    if start >= last:
        answer += 1
        last = end

print(answer)