import heapq

n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
arr.sort()

room = []
heapq.heappush(room, arr[0][1])

for i in range(1,n):
    # 같은 룸에서 할 수 있으면 그대로
    if arr[i][0] >= room[0]:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
    # 새로 룸 추가
    else:
        heapq.heappush(room, arr[i][1])

print(len(room))
