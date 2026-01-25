from collections import deque

connectedDict = {}


def findGroups(root, exc, n):
    global connectedDict
    
    visited = [False for _ in range(n)]
    q = deque([root])
    
    while q:
        next = q.popleft()
        
        if visited[next-1]:
            continue
        visited[next-1] = True
        
        for c in connectedDict[next]:
            if c != exc and not visited[c-1]:
                q.append(c)
    
    return visited.count(True)
    
    

def solution(n, wires):
    global connectedDict
    
    # 연결된 전력망 정보 dict 생성
    for i in range(1, n+1):
        connectedDict[i] = []
    
    for a, b in wires:
        connectedDict[a].append(b)
        connectedDict[b].append(a)
    
    # for i in range(1, n+1):
    #     print(f"connectedDict[{i}] : {connectedDict[i]}")
    
    result = 1000
    
    # 하나씩 잘라보기
    for d1, d2 in wires:
        # print(f"[DEBUG] {d1} {d2} 자르기")
        g1 = findGroups(d1, d2, n)
        g2 = findGroups(d2, d1, n)
        
        temp = g1-g2 if g1 > g2 else g2-g1
        result = min(result , temp)
        
    return result
        
        
        