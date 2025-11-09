import sys
from collections import deque
INF = 10 * 20001

input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().rstrip().split())
K = int(input().rstrip())

edges = {}

for i in range(1, V+1):
    edges[i] = []

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    
    edges[u].append((v, w))

# print(f"[Debug] edges : {edges}\n")

dp = [INF for _ in range(V)] # K로부터 최단 거리
is_visited = [0 for _ in range(V)] # 방문 여부
dp[K-1] = 0

for _ in range(V):
    visit_idx = -1
    for i in range(0, V):
        if is_visited[i] == 0 and (visit_idx == -1 or dp[i] <= dp[visit_idx]):
            visit_idx = i

    # print(f"[Debug] dp : {dp}\n")
    # print(f"[Debug] is_visited : {is_visited}\n")
    # print(f"[Debug] visit_idx : {visit_idx} 방문 \n")
    is_visited[visit_idx] = 1

    for v, w in edges[visit_idx+1]:
        dp[v-1] = min(dp[v-1], dp[visit_idx] + w)

for i in dp:
    print(F"{i if i != INF else 'INF'}\n")


        
        