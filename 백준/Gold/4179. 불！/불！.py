from collections import deque

MOVE = ((0, 1), (1, 0), (-1, 0), (0, -1))

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)] # j/f : 이미 지나간 경우


# =========== 불 위치 찾기
fireQ = deque([])
for x in range(R):
    for y in range(C):
        if board[x][y] == 'F':
            fireQ.append((x, y))

# =========== 불 업데이트
def fire():
    global board, R, C, fireQ, MOVE
    newQ = deque([])
    while fireQ:
        x, y = fireQ.popleft()
        for mx, my in MOVE:
            newX, newY = x+mx, y+my
            if 0<=newX < R and 0<=newY < C:
                if board[newX][newY] == "." or board[newX][newY] == "J":
                    board[newX][newY] = "F"
                    newQ.append((newX, newY))
    fireQ = newQ


def solution():
    global R, C, board, MOVE

    # =========== 시작 위치 찾기
    jPos = (0, 0)
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'J':
                jPos = (x,y)


    prevTime = -1
    q = deque([(jPos, 0)])

    while q:
        (prevX, prevY), time = q.popleft()

        # 끝에 도달한 경우
        if prevX == 0 or prevX == R-1 or prevY == 0 or prevY == C-1:
            return time+1
        
        if time > prevTime: # 불 먼저 이동
            fire()
            prevTime = time
        
        for mx, my in MOVE:
            newX, newY = prevX+mx, prevY+my
            if 0<=newX < R and 0<=newY < C and board[newX][newY] == ".":
                board[newX][newY] = "J"
                q.append(((newX, newY), time+1))
    return "IMPOSSIBLE"

print(solution())