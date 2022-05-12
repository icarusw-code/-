import heapq

def dijkstra(dist, graph):
    heap = []
    heapq.heappush(heap, [1, 0]) # 노드, 거리
    while heap:
        node, cost = heapq.heappop(heap)
        for n, c in graph[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [n, cost+c])
                
                
def solution(N, roads, K):
    answer = 0
    
    INF = int(10e9)
    dist = [INF] * (N+1)
    # 1번 출발이기 때문
    dist[1] = 0 
    graph = [[] for _ in range(N+1)]
    
    for road in roads:
        start, end, value = road
        # 양방향이므로 
        graph[start].append([end, value])
        graph[end].append([start, value])
	
    dijkstra(dist, graph)
	
    # 1에서 출발해서 각지점까지 거리
    # answer = [i for i in dist]
    
    # 문제에서 요구하는 K보다 작은 값
    answer = [i for i in dist if i <= K]

    return len(answer)