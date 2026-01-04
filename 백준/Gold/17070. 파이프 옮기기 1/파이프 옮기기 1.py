import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
room = []
for _ in range(N):
    room.append(list(map(int, input().rstrip().split())))

dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)] # 가로, 세로, 대각선
dp[0][0][0] = 1


shouldEmpty = ([(0, 0), (0, 1)],[(0, 0), (1, 0)], [(0, 0), (0, 1), (1, 0), (1, 1)]) # 가로, 세로, 대각선으로 배치하고자 할때 비어있어야 하는 칸 정보
canMove = ([(0, 1, 0), (0, 1, 2)], [(1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)]) # 가로, 세로, 대각선으로 배치되어 있는 상황에서 이동 가능한 방법


# toI , toJ : 이동시키고자 하는 위치의 시작 죄표
# dir : 이동 시키고자 하는 위치의 방향 (가로, 세로 대각선)
def move(toI, toJ, dir, way):
    global room, dp, shouldEmpty
    
    for idxI, idxJ in shouldEmpty[dir]:
        i = toI + idxI
        j = toJ + idxJ
        if i < 0 or i >= N or j < 0 or j >= N or room[i][j] != 0:
            return # 이동 불가능
            
    dp[toI][toJ][dir] += way

for i in range(N):
    for j in range(N):
        for dir in range(3):
            way = dp[i][j][dir]
        
            for idxI, idxJ, moveDir in canMove[dir]:
                move(i + idxI, j + idxJ, moveDir, way)


print(f"{dp[N-1][N-2][0] + dp[N-2][N-1][1] + dp[N-2][N-2][2]}")
        
        
        