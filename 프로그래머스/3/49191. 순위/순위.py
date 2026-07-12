from collections import deque
def solution(n, results):
    answer = 0
    
    inDegrees = [0 for i in range(n+1)]
    outEdges = [[] for i in range(n+1)]
    
    for x,y in results:
        inDegrees[y] += 1
        outEdges[x].append(y)
        
    dp = {}
    ranks = [set() for _ in range(n+1)]
    
    def DFS(curRank, leftNodes, inDegrees, outEdges):
        key = tuple(leftNodes)
        if key in dp:
            return
        dp[key] = 1
        
        for i, node in enumerate(leftNodes):
            if inDegrees[node] == 0:
                newLeftNodes = leftNodes[:i] + leftNodes[i+1:]
                
                for j in outEdges[node]:
                    inDegrees[j] -= 1
                
                ranks[node].add(curRank)
                DFS(curRank+1, leftNodes[:i] + leftNodes[i+1:], inDegrees, outEdges)
                
                for j in outEdges[node]:
                    inDegrees[j] += 1
    DFS(1, [i for i in range(1, n+1)], inDegrees, outEdges)
    
    for i in range(1, n+1):
        if len(ranks[i]) == 1:
            answer += 1
    return answer
        
    
        
        