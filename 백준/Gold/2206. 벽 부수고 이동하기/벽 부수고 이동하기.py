import sys
from collections import deque

INF = 10**6

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input().rstrip())))


# 시작 위치에서 이동 가능 거리 구하기
distance = [ [[-1, -1] for _ in range(M)] for _ in range(N)]

distance[0][0] = [1, -1]
q = deque([(0, 0, 1, 0)]) # x 좌표, y 좌표, 거리, 벽 부수기 여부

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while len(q) > 0:
    x, y, d, is_braked = q.popleft()

    # print(f"\n=== [Debug] x: {x}, y: {y} , d : {d}, is_braked : {is_braked} === \n\n")
    # print_arr(distance)
    for i, j in moves:
        if x + i >= 0 and x + i < N and y + j >= 0 and y + j < M:
            #print(F"[Debug] x+i : {x+i}, y+j : {y+j}")
            
            # 벽이 아닌 경우
            if maze[x+i][y+j] == 0:
                if distance[x+i][y+j][is_braked] == -1:
                    q.append((x+i, y+j, d+1, is_braked))
                    distance[x+i][y+j][is_braked] = d+1
                    #print(" => 벽이 아니다! 이동!\n")
                #else:
                    #print(" => 이미 왔었다..\n")
            elif not is_braked:
                # 벽이지만 아직 한번도 부수지 않은 경우
                if distance[x+i][y+j][1] == -1:
                    q.append((x+i, y+j, d+1, 1))
                    distance[x+i][y+j][1] = d+1
                    #print(" => 벽이다! 부수자!\n")
                #else:
                    #print(" => 이미 왔었다..\n")
            #else:
                #print("=> 벽이다.. 못 부순다.. \n")
    #print(f"[Debug] q : {q}\n")

# print_arr(distance)
if -1 in distance[N-1][M-1]:
    print(F"{max(distance[N-1][M-1])}")
else:
    print(F"{min(distance[N-1][M-1])}")
