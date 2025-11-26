import sys
from collections import deque
import copy

input = sys.stdin.readline
print = sys.stdout.write

## ========= 입력 값 입력 받기

N, M = map(int, input().rstrip().split())

m = []

for _ in range(N):
    m.append(list(map(int, input().rstrip().split())))

## ========= 

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

result = 0
def bfs():
    global m, moves,N, M, result
    
    new_m = copy.deepcopy(m)
    
    '''
    print("==== [DEBUG] new_m : \n")
    for line in new_m:
        print(f"   {line}\n")
    print("\n")
    '''

    virous = deque([])

    for i in range(N):
        for j in range(M):
            if new_m[i][j] == 2:
                virous.append((i, j))
    # print(f"[DEBUG] viorus : {virous}\n")

    while virous:
        x, y = virous.popleft()
        # rint(f"[DEBUG] x : {x}, y : {y}\n")

        for i , j in moves:
            # print(f"   [DEBUG] i : {i}, j: {j}")
            if 0 <= x+i and x+i < N and 0 <= y+j and y+j<M and new_m[x+i][y+j] == 0:
                # print(f" => m[x+i][y+j] : {m[x+i][y+j]}")
                new_m[x+i][y+j] = 2
                virous.append((x+i, y+j))
                # print(f"[DEBUG] viorus : {virous}\n")
            # print("\n")


    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_m[i][j] == 0:
                cnt += 1
    '''
    if cnt > result:
        for line in new_m:
            print(f"{line}\n")
        print("\n")
    '''     
    result = max(cnt, result)

    
                    
def makeWall(prevX, prevY, leftCnt):
    global N, M, m
    
    if leftCnt == 0:
        bfs()
        return

    for j in range(prevY, M):
        if m[prevX][j] == 0:
            m[prevX][j] = 3
            makeWall(prevX, j, leftCnt -1)
            m[prevX][j] = 0


    for i in range(prevX+1, N):
        for j in range(M):
            if m[i][j] == 0:
                m[i][j] = 3
                makeWall(i, j, leftCnt-1)
                m[i][j] = 0
                
makeWall(0, 0, 3)

print(f"{result}")
    
    