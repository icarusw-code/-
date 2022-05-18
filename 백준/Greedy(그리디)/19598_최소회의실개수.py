import heapq

n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

queue = []
arr.sort(key=lambda x: x[0])

for start, end in arr:
    if queue and start >= queue[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, end)

print(len(queue))