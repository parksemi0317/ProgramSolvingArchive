from collections import deque

def solution(n, infection, edges, k):
    start_bitMask = 0b1 << (infection- 1)
    
    # ================ 파이프 연결 정보 가공 (수정 필요)
    
    pipes = [{},{},{}]
    for x, y, t in edges:
        if x in pipes[t-1]:
             pipes[t-1][x].append(y)
        else:
             pipes[t-1][x] = [y]
        
        if y in pipes[t-1]:
             pipes[t-1][y].append(x)
        else:
             pipes[t-1][y] = [x]
    
    # 디버깅용 출력
    for p in pipes:
        print(p)
    
    # ================

    dp = {} # key : (감염 여부 bitMask, pipe_idx), value : 다음 bitMask

    # 해당 파이프를 열었을 때의 결과를 담은 bitMask를 구하는 함수
    def getNextBitMask(bitMask, pipe_idx):
        nonlocal dp, pipes, n
        
        if (bitMask, pipe_idx) in dp: # 이전에 연산한 경우
            return dp[(bitMask, pipe_idx)]
        
        new_bitMask = bitMask
        
        temp_q = deque([])
        is_inserted = [False] * n
        
        # 현재 감염된 노드들 큐에 삽입
        for i in range(n):
            i_bitMask = 0b1 << i
            if bitMask & i_bitMask:
                temp_q.append(i+1)
                is_inserted[i] = True
        
        while temp_q:
            cur_node = temp_q.popleft()

            if cur_node in pipes[pipe_idx]:
                for next_node in pipes[pipe_idx][cur_node]:
                    
                    if not is_inserted[next_node-1]:
                        temp_q.append(next_node) # 큐에 삽입
                        is_inserted[next_node-1] = True
                        new_bitMask = new_bitMask | (0b1 << (next_node-1))
        dp[(bitMask, pipe_idx)] = new_bitMask
        return new_bitMask
    
    # ================ 
    
    # bitMask 내에 감염된 배양체의 수를 구하는 함수
    def getAffactCnt(bitMask):
        result = 0
        while bitMask > 0:
            result += bitMask & 0b1
            bitMask = bitMask >> 1
        return result
    
    # ================ 
    q = deque([(start_bitMask, 0, -1)]) # 감염 bitMask, 파이프 오픈 횟수, 마지막으로 연 파이프 idx
    
    result = 1
    while q:
        bitMask, cnt, prev_pipe_idx = q.popleft()
        print(f"[DEBUG] {bitMask:b}, {cnt}, {prev_pipe_idx}")
        result = max(result, getAffactCnt(bitMask)) # 현재 감염체 개수
        
        if result == n:
            break
        
        # 더 열었다 닫았다 할 수 있는 경우
        if cnt < k:
            for i in range(3):
                if i != prev_pipe_idx: # 마지막으로 연 파이프가 아닌 경우
                    next_bitMask = getNextBitMask(bitMask, i)
                    
                    if bitMask != next_bitMask: # 변경된 값이 있는 경우 큐에 삽입
                        q.append((next_bitMask, cnt+1, i))
    return result