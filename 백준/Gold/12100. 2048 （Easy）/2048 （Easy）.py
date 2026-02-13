import sys

input = sys.stdin.readline
print = sys.stdout.write

# =================== 값 입력 받기 ===================

N = int(input().rstrip())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# =================== 이동 함수 ===================

def printBoard(board):
    for line in board:
        for c in line:
            print(F"{c} ")
        print("\n")
    print("\n")

def swapUp(board):
    global N

    newBoard = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        combI = -1 # 마지막으로 합쳐졌던 곳
        iIdx = -1 # 마지막으로 값이 들어간 곳
        for i in range(N):
            if board[i][j] ==0:
                continue
            elif iIdx != -1 and combI != iIdx and board[i][j] == newBoard[iIdx][j]:
                # 이전 블록과 합칠 수 있는 경우 합치기
                newBoard[iIdx][j] *= 2
                combI = iIdx
            else:
                iIdx += 1
                newBoard[iIdx][j] = board[i][j]
    # print("swapUp : \n")
    # printBoard(board)
    # printBoard(newBoard)
    return newBoard

def swapDown(board):
    global N

    newBoard = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):
        combI = N # 마지막으로 합쳐졌던 곳
        iIdx = N # 마지막으로 값이 들어간 곳
        for i in range(N-1, -1, -1):
            if board[i][j] ==0:
                continue
            elif iIdx != N and combI != iIdx and board[i][j] == newBoard[iIdx][j]:
                newBoard[iIdx][j] *= 2
                combI = iIdx
            else:
                iIdx -= 1
                newBoard[iIdx][j] = board[i][j]
    # print("swapDown : \n")
    # printBoard(board)
    # printBoard(newBoard)
    
    return newBoard

def swapRight(board):
    global N

    newBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        combJ = N
        jIdx = N
        for j in range(N-1, -1, -1):
            if board[i][j] ==0:
                continue
            elif jIdx != N and jIdx != combJ and board[i][j] == newBoard[i][jIdx]:
                newBoard[i][jIdx] *= 2
                combJ = jIdx
            else:
                jIdx -= 1
                newBoard[i][jIdx] = board[i][j]

    # print("swapRight : \n")
    # printBoard(board)
    # printBoard(newBoard)
    return newBoard

def swapLeft(board):
    global N

    newBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        jIdx = -1
        combJ = -1
        for j in range(N):
            if board[i][j] == 0:
                continue
            if jIdx != -1 and jIdx != combJ and board[i][j] == newBoard[i][jIdx]:
                newBoard[i][jIdx] *= 2
                combJ = jIdx
            else:
                jIdx += 1
                newBoard[i][jIdx] = board[i][j]
    # print("swapLeft : \n")
    # printBoard(board)
    # printBoard(newBoard)
    
    return newBoard

# ===================  ===================
result = 0

def DFSSearch(board, moveCnt):
    global result
    
    if moveCnt >= 5:
        result = max(result, max([ max(line) for line in board]))
        return

    DFSSearch(swapUp(board), moveCnt+1)
    DFSSearch(swapDown(board), moveCnt+1)
    DFSSearch(swapLeft(board), moveCnt+1)
    DFSSearch(swapRight(board), moveCnt+1)


DFSSearch(board, 0)
print(f"{result}")
# =================== 테스트 ===================
