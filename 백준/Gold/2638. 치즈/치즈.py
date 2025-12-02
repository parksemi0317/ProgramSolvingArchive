import sys
import copy
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

grid = []
cheezeCnt = 0

for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    cheezeCnt += line.count(1)
    grid.append(line)
'''
def printGrid():
    global grid

    for line in grid:
        for c in line:
            print(f"{c}".rjust(3))
        print("\n")
    print("\n")
'''

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    
time = 0
while cheezeCnt > 0:
    time += 1
    # print(f"\n================== time : {time} ==================\n")
    # printGrid()
    
    tempGrid = copy.deepcopy(grid)
    # 각 치즈가 외부와 닿는 면적 수 구하기
    q = deque([(0, 0), (N-1, 0), (0, M-1), (N-1, M-1)])
    tempGrid[0][0] = tempGrid[N-1][0] = tempGrid[0][M-1] = tempGrid[N-1][M-1] = -1
    
    delCheeze = [] # 녹을 치즈 목록

    while q:
        x, y = q.popleft()

        for mx, my in moves:
            newX = x + mx
            newY = y + my
            if 0 <= newX and newX < N and 0 <= newY and newY < M:
                if grid[newX][newY] == 0 and  tempGrid[newX][newY] == 0:
                    q.append((newX, newY)) # 공기인 경우 큐에 삽입
                    tempGrid[newX][newY] = -1 # 공기 방문 완료 체크
                elif grid[newX][newY] == 1:
                    # 치즈인 경우
                    tempGrid[newX][newY] += 1
                    if tempGrid[newX][newY] ==3:
                        delCheeze.append((newX, newY)) # 녹을 치즈 목록에 삽입

    '''
    for line in tempGrid:
        for c in line:
            print(f"{-1 if c >= 3 else (0 if c == -1 else 1 )}".rjust(3))
        print("\n")
    print("\n")
    '''
    
    for x, y in delCheeze:
        grid[x][y] = 0
        cheezeCnt -= 1
print(f"{time}")