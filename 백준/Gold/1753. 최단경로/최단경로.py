import sys
INF = 10 * 20001 # 최대 거리

# 다익스트라

input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().rstrip().split())
K = int(input().rstrip())

edges = {} # 이동 가능 간선 dict (도착 정점, 가중치) 배열

# edges 초기화
for i in range(1, V+1):
    edges[i] = []

# 간선 입력 받기
for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    
    edges[u].append((v, w))

dp = [INF for _ in range(V)] # K로부터 최단 거리
is_visited = [0 for _ in range(V)] # 방문 여부
dp[K-1] = 0 # 시작 위치 거리 0으로 초기화

for _ in range(V):
    # 아직 방문하지 않은 정점 중 경로 길이가 가장 짧은 정점 찾기
    visit_idx = -1
    for i in range(0, V):
        if is_visited[i] == 0 and (visit_idx == -1 or dp[i] <= dp[visit_idx]):
            visit_idx = i

    is_visited[visit_idx] = 1

    # 해당 정점에서 이동 가능한 정점의 최단 거리 갱신
    for v, w in edges[visit_idx+1]:
        dp[v-1] = min(dp[v-1], dp[visit_idx] + w)

# 결과 출력
for i in dp:
    print(F"{i if i != INF else 'INF'}\n")


        
        