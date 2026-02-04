import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

parents = [i for i in range(n)]

def findRoot(i):
    global parents

    iterI = i
    while parents[iterI] != iterI:
        iterI = parents[iterI]
        
    parents[i] = iterI # 평탄화 작업
    return iterI

def solution():
    global parents, m
    
    for i in range(m):
        a, b = map(int, input().strip().split())

        
        aRoot = findRoot(a)
        bRoot = findRoot(b)

        if aRoot == bRoot: # 동일한 그룹 안에 있는 경우 (사이클 발생)
            return i+1 

        # 두 그룹 합치기
        if aRoot < bRoot:
            parents[aRoot] = bRoot
        else:
            parents[bRoot] = aRoot
        
    return 0
print(solution())
