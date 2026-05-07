def solution(n, lost, reserve):
    
    cur = [1 for _ in range(n)]
    
    for l in lost:
        cur[l-1] = 0
    
    for r in reserve:
        cur[r-1] += 1
    
    print(cur)
    
    nonCnt = 0
    if cur[0] == 0:
        if cur[1] == 2:
            cur[0] = cur[1] = 1
        else:
            nonCnt += 1
    
    for i in range(1, n-1):
        
        if cur[i] == 0:
            if cur[i-1] == 2:
                cur[i-1] = cur[i] = 1
            elif cur[i+1] == 2:
                cur[i+1] = cur[i] = 1
            else:
                nonCnt += 1
    if cur[n-1] == 0 and cur[n-2] < 2:
        nonCnt += 1
    return n -nonCnt 
        