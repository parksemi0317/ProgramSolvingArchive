import sys
from collections import deque

INF = 10**6
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
print = sys.stdout.write

# ========= 입력 값 받기 =========
N, M = map(int, input().rstrip().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input().rstrip())))


# ========= DFS =========
# 시작 위치에서 도달 가능 거리 배열
# distance[x][y] : (벽을 한번도 부수지 않고 도달 가능 거리, 1번 부수고 도달 가능 거리)
distance = [ [[-1, -1] for _ in range(M)] for _ in range(N)]

# 시작 위치 값 설정
distance[0][0] = [1, -1]

# dfs용 큐
# (x 좌표, y 좌표, 거리, 벽 부수기 여부)
q = deque([(0, 0, 1, 0)])

# 상하좌우 이동 배열
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while len(q) > 0:
    x, y, d, is_braked = q.popleft()

    for i, j in moves:
        if x + i >= 0 and x + i < N and y + j >= 0 and y + j < M:
            
            # 벽이 아닌 경우
            if maze[x+i][y+j] == 0:
                if distance[x+i][y+j][is_braked] == -1:
                    q.append((x+i, y+j, d+1, is_braked))
                    distance[x+i][y+j][is_braked] = d+1
            elif not is_braked:
                # 벽이지만 아직 한번도 부수지 않은 경우
                if distance[x+i][y+j][1] == -1:
                    q.append((x+i, y+j, d+1, 1))
                    distance[x+i][y+j][1] = d+1

# ========= 최소 거리 출력 =========

if -1 in distance[N-1][M-1]:
    print(F"{max(distance[N-1][M-1])}")
else:
    print(F"{min(distance[N-1][M-1])}")
