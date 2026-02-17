import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# =============== 값 입력 받기 ===============

# ===== N값 입력 받기
N = int(input().rstrip())

# 0 : 빈공간
# 1 : 뱀
# -1 : 사과
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1

K = int(input().rstrip())

# ===== 사과 위치 입력 받기
for _ in range(K):
    i, j = map(int, input().rstrip().split())
    board[i-1][j-1] = -1

# ===== 방향 변환 입력 받기
rotates = deque([])

L = int(input().rstrip())
for _ in range(L):
    rotates.append(list(input().rstrip().split()))

# =============== 디버깅용 ===============

def printBoard():
    global board

    for line in board:
        for c in line:
            print(F"{c}".rjust(3))
        print("\n")
    print("\n")
# printBoard()

# =============== 뱀 이동 ===============
time = 0
head = (0, 0)
tail = (0, 0)

MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))
moveIdx = 0

# ===== 함수 =====

# 방향 전환
def rotate(dir):
    global moveIdx

    if dir == "D":
        moveIdx = (moveIdx + 1) % 4
    elif dir == "L":
        moveIdx = (moveIdx + 3) % 4

def findTail(curTail):
    global board, MOVES, N

    for i, j in MOVES:
        next = (curTail[0] + i, curTail[1] + j)
        if 0 <= next[0] < N and 0 <= next[1] < N:
            if board[next[0]][next[1]] == board[curTail[0]][curTail[1]] + 1:
                return next
    return (-1, -1)  

def move():
    global board, moveIdx, head, tail, MOVES
    curMove = MOVES[moveIdx]

    nextHead = (head[0] + curMove[0], head[1] + curMove[1])
    # print(f"[DEBUG] nextHead : {nextHead}\n")

    # 머리가 벽에 부딛히는 경우
    if 0 > nextHead[0] or nextHead[0] >= N or 0 > nextHead[1] or nextHead[1] >= N:
        return -1
    
    if board[nextHead[0]][nextHead[1]] == 0:
        # 비어있는 경우
        board[nextHead[0]][nextHead[1]] = board[head[0]][head[1]] + 1
        head = nextHead

        newTail = findTail(tail) # 다음 꼬리 찾기
        board[tail[0]][tail[1]] = 0 # 기존 꼬리 지우기
        tail = newTail
        
    elif board[nextHead[0]][nextHead[1]] == -1:
        # 사과가 있는 경우
        board[nextHead[0]][nextHead[1]] = board[head[0]][head[1]] + 1
        head = nextHead
    else:
        # 자신의 몸통에 부딛히는 경우
        return -1
    
    return 1

# ===== 풀이 =====

def solution():
    global rotates, time
    
    while rotates:
        rotateTime, rotateDir = rotates.popleft()
        
        rotateTime = int(rotateTime)
        # print(f"======== [DEBUG] rotateTime : {rotateTime} , rotateDir : {rotateDir} ========\n")
        
        while time < rotateTime:
            # print(f"=== [DEBUG] time : {time} ===\n")
            if move() == -1: # 한칸 이동
                return
            time += 1
            # printBoard()
        # 방향전환
        rotate(rotateDir)

    while move() != -1:
        time += 1
        # printBoard()
    return

solution()
print(f"{time + 1}")