import heapq

def solution(n, works):
    # n : 남은 시간, works : 일의 작업량
    works = [-w for w in works]
    heapq.heapify(works)
    
    for i in range(n):
        maxIdx = 0 
        
        w = heapq.heappop(works)
        if w >= 0:
                return 0
        heapq.heappush(works, w+1)
    
    result = 0
    for w in works:
        result += w * w
    return result