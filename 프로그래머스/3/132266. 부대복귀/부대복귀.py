import heapq

def solution(n, roads, sources, destination):
    roadMatrix = [[] for _ in range(n+1)]
    # ======= roads 가공
    for a, b in roads:
        roadMatrix[a].append(b)
        roadMatrix[b].append(a)
        
    # ======= 다익스트라
    INF = n * n
    distances = [INF for _ in range(n+1)]
    distances[destination] = 0
    
    q = [(0, destination)]
    qVisited = [False for _ in range(n+1)]
    
    while q:
        _, cur = heapq.heappop(q)
        
        if qVisited[cur]:
            continue
        
        for nxt in roadMatrix[cur]:
            if qVisited[nxt]:
                continue
            if distances[nxt] > distances[cur]+1:
                distances[nxt] = distances[cur] + 1
                heapq.heappush(q, (distances[nxt], nxt))
    
        
        
    # ======= 결과 개산
    
    answer = []
    for s in sources:
        if distances[s] == INF:
            answer.append(-1)
        else:
            answer.append(distances[s])
    return answer