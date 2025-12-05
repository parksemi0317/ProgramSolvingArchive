import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

INF = 21 * 21


## =============== 입력 값 받기

N = int(input().rstrip())

shark = [] # 현재 상어 위치
sea = []


for i in range(N):
    line = list(map(int, input().rstrip().split()))
    
    # 상어는 제외하고 저장
    for j in range(N):
        if line[j] == 9:
            shark = (i, j)
            line[j] = 0
    
    sea.append(line)
    

## =============== 디버깅용 출력

'''
print(f"[DEBUG] shark : ({shark[0]},{shark[1]}), sea : \n")
for line in sea:
    for d in line:
        print(f"{d}".rjust(3))
    print("\n")
print("\n")
'''

## =============== 

sharkSize = 2
eatCnt = 0
time = 0
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while 1:
    # print(f"\n======== [DEBUG] time : {time} / sharkSize : {sharkSize}\n")
    # print(f"[DEBUG] shark : {shark}\n")
    # print(f"[DEBUG] shark : {shark}, sea : \n")
    '''
    for line in sea:
        for d in line:
            print(f"{d}".rjust(3))
        print("\n")
    print("\n")
    '''

    
    # ====== 먹을 수 있는 물고기 목록 찾기 (BFS)
    canEat = []
    minDist = INF

    q = deque([shark])
    dist = [[INF for _ in range(N)] for _ in range(N)] # 거리
    dist[shark[0]][shark[1]] = 0

    while q:
        i, j = q.popleft()
        
        # print(f"[DEBUG] i, j : {i}, {j}\n")

        if minDist <= dist[i][j]:
            # print("[DEBUG] BFS 종료\n")
            break

        for mI, mJ in MOVES:
            nextI = i + mI
            nextJ = j + mJ
            if 0 <= nextI < N and 0 <= nextJ < N and dist[nextI][nextJ] == INF:
                if sea[nextI][nextJ] == 0 or sea[nextI][nextJ] == sharkSize:
                    dist[nextI][nextJ] = dist[i][j] + 1
                    q.append((nextI, nextJ))
                elif sea[nextI][nextJ] < sharkSize:
                    dist[nextI][nextJ] = dist[i][j] + 1
                    minDist = dist[nextI][nextJ]
                    canEat.append((nextI, nextJ))
    '''          
    print("[DEBUG] dist : \n")
    for line in dist:
        for d in line:
            print(f"{d if d < INF else 'INF'}".rjust(4))
        print("\n")
    print("\n")
    
    print(f"[DEBUG] canEat : {canEat}\n")
    '''
    
    # ======더이상 먹을 수 있는 물고기가 없는 경우
    if minDist == INF:
        break

    i, j = min(canEat) # 가장 가까운 물고기 구하기
    # print(f"먹을 수 있는가장 가까운 물고기 : {i}, {j} (size : {sea[i][j]})\n")
    # print(f"거리 : {minDist}\n")

    # ====== 잡아먹기
    time += minDist
    eatCnt += 1
    if sharkSize == eatCnt:
        sharkSize += 1
        eatCnt = 0
    shark = (i, j)
    sea[i][j] = 0


print(f"{time}")
    