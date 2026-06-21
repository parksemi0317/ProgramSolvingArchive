def getRoot(x, parents):
    if parents[x] == x:
        return x
    parents[x] = getRoot(parents[x], parents)
    return parents[x]
    
        
def solution(n, computers):
    parents = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                iRoot = getRoot(i, parents)
                jRoot = getRoot(j, parents)
                if iRoot < jRoot:
                    parents[jRoot] = iRoot
                else:
                    parents[iRoot] = jRoot
    s = set()
    for i in range(n-1, -1, -1):
        s.add(getRoot(i, parents))
    return len(s)
