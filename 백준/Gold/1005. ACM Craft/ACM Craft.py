import sys
from collections import deque

INF = 100000 * 1001

input = sys.stdin.readline

T = int(input().rstrip())

for tk in range(T):
    # print(f"===============[TEST CASE {tk + 1}]================")
    
    ## ============= 값 입력 받기 & 입력 값 가공
    N, K = map(int, input().rstrip().split())

    D = list(map(int, input().rstrip().split()))

    prevs = {} # 각 edge의 선행 edge
    leftPrevEdgeCnt = [0 for _ in range(N)]
    nexts = {} # 각 edge의 후행 edge

    for i in range(1, N+1):
        prevs[i] = [] 
        nexts[i] = []
    
    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        prevs[Y].append(X)
        nexts[X].append(Y)
        leftPrevEdgeCnt[Y-1] += 1

    W = int(input().rstrip())
    
    ## ============= 확인용 출력
    '''
    for i in range(1, N+1):
        print(f"[DEBUG] prevs[{i}]  : {prevs[i]}")
    print()
    for i in range(1, N+1):
        print(f"[DEBUG] nexts[{i}]  : {nexts[i]}")
    print()
    '''
    ## ============= 
    
    edgeTimes = [INF for _ in range(N)]
    q = deque([])

    for i in range(1, N+1):
        if leftPrevEdgeCnt[i-1] == 0:
            q.append(i)

    # print(f"[DEBUG] prev가 없는 edges : {q}")

    while q:
        edge = q.popleft()
        # print(f"\n==== [DEBUG] edge : {edge} =====")

        # 선행 edge들을 기준으로 현재 edge 완공 시기 구하기
        maxPrevTime = 0
        for p in prevs[edge]:
            maxPrevTime = max(maxPrevTime, edgeTimes[p-1] if edgeTimes[p-1] < INF else 0)

        edgeTimes[edge-1] = maxPrevTime + D[edge-1]
        # print(f"[DEBUG] edgeTimes : {edgeTimes}")

        if(edge == W):
            break
        
        # 후행 edge들 처리
        for n in nexts[edge]:
            leftPrevEdgeCnt[n-1] -= 1
            if leftPrevEdgeCnt[n-1] ==0:
                q.append(n)
                
        # print(f"[DEBUG] leftPrevEdgeCnt : {leftPrevEdgeCnt}")
        
        # print(f"[DEBUG] q : {q}")

    print(f"{edgeTimes[W-1]}")
        
        

        

