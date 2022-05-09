from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    result = 1
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == False:
                result += 1
                visited[i] = True
                queue.append(i)
    return result
    
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, cut in wires:
        visited = [False] * (n+1)
        visited[cut] = True
        result = bfs(start, visited, graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
        
        
    return answer