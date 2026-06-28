from collections import deque

def solution(n, costs):
    costs = deque(sorted(costs, key=lambda x:x[2]))
    
    result = 0 # 전체 소요 건설비용
    addCnt = 0 # 추가된 다리 개수
    
    root = [i for i in range(n+1)] # 분리 집합
    
    def getRoot(x): # 분리 집합 루트 구하는 함수 (재귀)
        if root[x] == x:
            return x
        
        result = getRoot(root[x])
        root[x] = result
        return root[x]   
    
    while costs:
        if addCnt == n-1:
            return result
        
        x1, x2, c = costs.popleft()
        
        root1 , root2 = getRoot(x1), getRoot(x2)
        if root1 != root2:
            result += c
            if root1 < root2:
                root[root2] = root1
            else:
                root[root1] = root2
    return result
            
        