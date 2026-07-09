from collections import deque
def solution(n, edge):
    
    # ========= 간선 포맷팅
    connected = [[] for _ in range(n+1)]
    for x,y in edge:
        connected[x].append(y)
        connected[y].append(x)
    
    # ========= 간선 정리
    q = deque([(1, 0)])
    
    distMap = {}
    distMap[1] = 0
    distArr = [[] for _ in range(n+1)]
    distArr[0].append(1)
    maxDist = 0
    
    while q:
        cur, dist = q.popleft()
        
        for nextVertex in connected[cur]:
            
            if nextVertex in distMap:
                 continue
                
            distMap[nextVertex] = dist + 1
            distArr[dist+1].append(nextVertex)
            maxDist = max(maxDist, dist+1)
            q.append((nextVertex, dist+1))
    
    return len(distArr[maxDist])