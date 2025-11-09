import sys
sys.setrecursionlimit(10**6)


input = sys.stdin.readline
print = sys.stdout.write

V = int(input().rstrip())

edges = [[] for _ in range(V)] # 간선 정보 (이동 가능 간선, 가중치) 배열

for _ in range(V):
    temp_input = list(map(int, input().rstrip().split()))
    s = temp_input[0]

    idx = 1
    child_cnt = 0
    while(temp_input[idx] != -1):
        e, t = temp_input[idx], temp_input[idx+1]
        edges[s-1].append((e, t))
        idx += 2

# ======== DFS ========
depth = [-1 for _ in range(V)] # 거리 정보

def Search(e, t):
    global visited, edges, depth
    
    depth[e-1] = t

    result = 0
    for to, time in edges[e-1]:
        if depth[to-1] == -1:
            Search(to, t + time)

# ======== 1번째 노드를 root로 두고 DFS ========

Search(1, 0) # 1번째 노드를 root로 두고 탐색
# print(f"[Debug] depth : {depth}\n")

# ======== 깊이가 가장 깊은 말단 노드 찾기 ========
max_idx = 0
for i in range(1, V):
    if depth[i] > depth[max_idx]:
        max_idx = i

# print(f"[Debug] max_idx : {max_idx}\n")

# ======== 깊이가 가장 깊은 말단 노드를 root로 두고 DFS ========
depth = [-1 for _ in range(V)] # 거리 정보

Search(max_idx+1, 0)
# print(f"[Debug] depth : {depth}\n")

print(F"{max(depth)}")
    
    