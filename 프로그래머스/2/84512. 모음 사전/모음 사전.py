import heapq

def solution(word):
    CARDS = ["A", "E", "I", "O", "U"]
    
    hq = ["A", "E", "I", "O", "U"]
    heapq.heapify(hq)
    
    cnt = 0
    while hq:
        next = heapq.heappop(hq)
        # print("next : ", next)
        
        cnt += 1
        if next == word:
            return cnt
        
        if len(next) < 5:
            
            for c in CARDS:
                heapq.heappush(hq, next + c)