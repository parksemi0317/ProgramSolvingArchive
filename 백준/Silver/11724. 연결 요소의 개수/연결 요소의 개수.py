import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 연결 여부 표시 이차원 배열
graph = [[0 for _ in range(N)]for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u-1][v-1] = graph[v-1][u-1] = 1

# 각 정점의 순회 여부
is_grouped = [0 for _ in range(N)]
group_cnt = 0

def search(edge):
    global graph, is_grouped, N

    is_grouped[edge] = 1

    for i in range(N):
        if graph[edge][i] == 1 and is_grouped[i] == 0:
            search(i)

for edge in range(N):
    if is_grouped[edge] == 0:
        group_cnt += 1
        search(edge)

print(group_cnt)
