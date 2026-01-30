import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write


# ==================== 값 입력 받기 ====================

N, M = map(int,input().rstrip().split())

bridges = []

for _ in range(M):
    A, B, C = map(int,input().rstrip().split())

    bridges.append((C, A, B))


# ==================== 최소 신장 트리 (1개 제외) 구하기 ====================

bridges.sort()
parents = [i+1 for i in range(N)]
result = 0

def findRoot(k):
    global parents
    if parents[k-1] == k:
        return k
    return findRoot(parents[k-1])
    

i = 0
for _ in range(N-2):
    while True:
        w, a, b = bridges[i]
        i += 1

        aRoot = findRoot(a)
        bRoot = findRoot(b)
        if aRoot!= bRoot:
            if aRoot < bRoot:
                parents[bRoot-1] = aRoot
            else:
                parents[aRoot-1] = bRoot
            result += w
            break

print(f"{result}")