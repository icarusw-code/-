import heapq
# //....
# 추가
def dijkstra(dist, graph):
    heap = []
    heapq.heappush(heap, [1,0]) # 노드, 값
    
    while heap:
        node, cost = heapq.heappop(heap)
        
        for n, c in graph[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [n, cost + c])
    
def solution(n, edges):
    answer = 0
    INF = int(1e9)
    dist = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    dist[1] = 0
    
    for edge in edges:
        start, end = edge
        graph[start].append([end, 1])
        graph[end].append([start, 1])
        
    dijkstra(dist, graph)        
    
    for i in dist:
        if max(dist[1:]) == i:
            answer += 1
    return answer