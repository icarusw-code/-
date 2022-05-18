import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    heapq.heapify(arr)

    while len(arr) > 1:
        f1, f2 = 0, 0
        f1 += heapq.heappop(arr)
        f2 += heapq.heappop(arr)
        answer += f1+f2
        heapq.heappush(arr, f1+f2)
    
    print(answer)