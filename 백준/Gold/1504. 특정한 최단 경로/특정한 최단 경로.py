import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write
INF = int(1e9)

N , E = map(int, input().rstrip().split())

# ========== 간선 입력 받기

edges = [[INF for _ in range(N)] for _ in range(N)] # 간선 이차원 배열

for v in range(N):
    edges[v][v] = 0

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    
    edges[a-1][b-1] = edges[b-1][a-1] = min(edges[a-1][b-1], c)

# 디버깅용 출력
'''
for line in edges:
    for num in line:
        print(F"{str(num) + '  ' if num < INF else 'INF'}  ")
    print("\n")
print("\n")
'''


# ========== v1, v2 입력 받기
v1, v2 = map(int, input().rstrip().split())


# ========== 다익스트라
def getDists(start):
    global edges, N

    dist1 = [INF for _ in range(N)] # 1번 정점에서의 거리
    dist1[start-1] = 0
    
    q = [(0, start)]
    visited = [False for _ in range(N)]
    
    for i in range(N):
        if not q:
            break
        
        d, cur = heapq.heappop(q)
        visited[cur-1] = True
    
        for to in range(N):
            if edges[cur-1][to-1] != INF and dist1[to-1] > dist1[cur-1] + edges[cur-1][to-1]:
                dist1[to-1] = dist1[cur-1] + edges[cur-1][to-1]
                heapq.heappush(q, (dist1[to-1], to))
    return dist1

dist1 = getDists(1) # 1번 정점에서의 거리 구하기
dist2 = getDists(N) # N번 정점에서의 거리 구하기
dist3 = getDists(v1) # v1번 정점에서의 거리 구하기

# print(f"[DEBUG] dist1 :{dist1}\n")
# print(f"[DEBUG] dist2 :{dist2}\n")
# print(f"[DEBUG] dist3 :{dist3}\n\n")
 
# ========== 
if dist3[v2-1] >= INF:
    print("-1")
else:
    v1v2 = dist1[v1-1] + dist3[v2-1] + dist2[v2-1]
    v2v1 = dist1[v2-1] + dist3[v2-1] + dist2[v1-1]
    
    if v1v2 >= INF or v2v1 >= INF:
       print("-1") 
    else:
        print(f"{min(v1v2, v2v1)}")
