import heapq
import numpy as np

def solution(signals):
    signal_len = len(signals)
    
    # ========= 절대 안겹치는 경우 찾기
    max_time =  np.lcm.reduce([sum(s) for s in  signals])
    
    # ========= 
    
    # (시작 지점, signal idx) 형식의 heapq
    hq = [ (g,idx) for idx, (g, y, r) in enumerate(signals)] 
    heapq.heapify(hq)
    
    cur_range = (-1, -1) # 현재 보고 있는 중복 노란불 범위의 시작, 종료 시간
    is_yellow = [False] * signal_len
    yellow_cnt = 0
    
    while hq:
        nextStart, nextIdx = heapq.heappop(hq)
        
        if nextStart > max_time:
            return -1
        
        nextEnd = nextStart+signals[nextIdx][1]-1
        if cur_range[0] <= nextStart <= cur_range[1]: # 범위에 속하는 경우
            if not is_yellow[nextIdx]:
                is_yellow[nextIdx] = True
                yellow_cnt += 1
                
                if yellow_cnt == signal_len:
                    return max(cur_range[0], nextStart) + 1
            # 중복 범위 업데이트
            cur_range = (max(cur_range[0], nextStart), min(cur_range[1], nextEnd))
        else: # 범위에 속하지 않는 경우 현재 yellow 기준으로 초기화
            cur_range = (nextStart, nextEnd)
            is_yellow = [False] * signal_len
            is_yellow[nextIdx] = True
            yellow_cnt = 1
            
        heapq.heappush(hq, (nextStart + sum(signals[nextIdx]), nextIdx)) # 다음 시작 지점 push
    return -1