import sys
from collections import deque
import copy

input = sys.stdin.readline
print = sys.stdout.write

# ================= 값 입력 받기 =================

N, M = map(int, input().rstrip().split())

board = []

for _ in range(N):
    board.append(list(input().rstrip()))
        

# ================= 초기 큐 세팅 =================

q = deque([[0,0,0, board]]) # 이동 횟수, 빨간 공 위치, 파란공 위치, 보드 전체
hole = [-1, -1]
for i in range(1, N-1):
    for j in range(1, M-1):

        if board[i][j] == 'B':
            q[0][2] = (i, j)
        elif board[i][j] == "R":
            q[0][1] = (i, j)
        elif board[i][j] == "O":
            hole = (i, j)

# print(f"[DEBUG] 초기 q : {q}\n")

# ================= 기울이기 함수 =================
DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))# 상, 하, 좌, 우

# 구멍에 빠진 경우 (-1, -1)반환
# 그 외의 경우 이동하게되는 위치 반환
# board 자동 갱신
def moveBall(move, position, board):
    prev = board[position[0]][position[1]]
    newP = [position[0], position[1]]
    newBoard = copy.deepcopy(board)
    while True:
        if 0 < newP[0] + move[0] < N-1 and 0 < newP[1] + move[1] < M-1:
            if board[newP[0] + move[0]][newP[1] + move[1]] == ".":
                newBoard[newP[0]][newP[1]] = "."
                newP[0] += move[0]
                newP[1] += move[1]
                newBoard[newP[0]][newP[1]] = prev
            elif board[newP[0] + move[0]][newP[1] + move[1]] == "O":
                newBoard[newP[0]][newP[1]] = "."
                return ((-1, -1), newBoard) # 구멍에 빠진 경우
            else: # 벽이나 공에 닿은 경우
                break
        else: # 경계 벽에 닿은 경우
            break
    return newP, newBoard


# 1 : 빨간 공이 빠진 경우 (파란공은 빠지지 X)
# -1 : 파란 공이 빠진 경우 (빨간 공도 빠졌을 수도)
# [0, 빨간공 위치, 파란공 위치, 전체 보드판] : 아무것도 빠지지 않음
def tilt(dir, red, blue, board):
    global DIR, N, M, result, hole
    move = DIR[dir]

    if(move[0] == 0 and (red[1] - blue[1]) * move[1] > 0) or (move[1] == 0 and (red[0] - blue[0]) * move[0] > 0):
        # 빨간 공 먼저 이동
        redResult, board = moveBall(move, red, board)
        blueResult, board = moveBall(move, blue, board)
        # print(f"[DEBUG] {dir} red first => redResult : {redResult}, blueResult : {blueResult}\n")
    else:
        # 파란 공 먼저 이동
        # print(f"[DEBUG] {dir} blue first\n")
        blueResult, board = moveBall(move, blue, board)
        redResult, board = moveBall(move, red, board)

    if blueResult[0] == -1:
        return [-1,]
    if redResult[0] == -1:
        return [1,]
    return [0, redResult, blueResult, board]            
            
            

# ================= BFS =================

def solution():
    global result
    while q:
        moveCnt, red, blue, board = q.popleft()
        # print(f"[DEBUG] moveCnt : {moveCnt}, red : {red}, blue : {blue}\n")
        for dir in range(4):
            tiltResult = tilt(dir, red, blue, board)

            if tiltResult[0] == 1:
                # print(f"[DEBUG] dir : {dir}\n")
                return moveCnt + 1 # 빨간 공만 빠진 경우
            elif tiltResult[0] == -1:
                continue # 파란공이 빠진 경우
            else:
                if moveCnt < 9:
                    if not (tiltResult[1][0] == red[0] and tiltResult[1][1] == red[1]) or not (tiltResult[2][0] == blue[0] and tiltResult[2][1] == blue[1]):
                        q.append([moveCnt+1 ,tiltResult[1], tiltResult[2], tiltResult[3]])
                        # print(f"[DEBUG] dir : {dir}, red : {tiltResult[1]}, blue : {tiltResult[2]}\n")
    return -1

print(F"{solution()}")
