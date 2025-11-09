import sys
INF = 100 * 10001

input = sys.stdin.readline
print = sys.stdout.write

N, M, X = map(int, input().rstrip().split())

edges = {}
rev_edges = {}

for i in range(1, N+1):
    edges[i] = []
    rev_edges[i] = []

for i in range(M):
    s, e, t = map(int, input().rstrip().split())
    edges[s].append((e, t))
    rev_edges[e].append((s, t))

# 집에서 X로 가는 최단거리
rev_dp = [INF for _ in range(N)]
is_visited = [0 for _ in range(N)]
rev_dp[X-1] = 0

for i in range(N):
    visit_idx = -1
    for j in range(N):
        if is_visited[j] == 0 and (visit_idx == -1 or rev_dp[j] < rev_dp[visit_idx]):
            visit_idx = j
    # print(F"[Debug] visit_idx : {visit_idx}\n")
    is_visited[visit_idx] = 1

    for e, t in rev_edges[visit_idx+1]:
        rev_dp[e-1] = min(rev_dp[e-1], rev_dp[visit_idx] + t )
    # print(f"[Debug] rev_dp : {rev_dp}\n")

# X에서 집으로 돌아가는 최단거리
dp = [INF for _ in range(N)]
is_visited = [0 for _ in range(N)]
dp[X-1] = 0

for i in range(N):
    visit_idx = -1
    for j in range(N):
        if is_visited[j] == 0 and (visit_idx == -1 or dp[j] < dp[visit_idx]):
            visit_idx = j
    # print(F"[Debug] visit_idx : {visit_idx}\n")
    is_visited[visit_idx] = 1

    for e, t in edges[visit_idx+1]:
        dp[e-1] = min(dp[e-1], dp[visit_idx] + t )
    # print(f"[Debug] dp : {dp}\n")

print(f"{max([dp[i] + rev_dp[i] for i in range(N)])}")
