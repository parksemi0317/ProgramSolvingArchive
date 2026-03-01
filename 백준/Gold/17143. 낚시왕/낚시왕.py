import sys

input = sys.stdin.readline
print = sys.stdout.write

# =============== 값 입력 받기 ===============

R, C, M = map(int, input().rstrip().split())

sharks = []
# 상어 정보
for _ in range(M):
    r, c, s, d, z = map(int, input().rstrip().split())
    if d == 1 or d == 2:
        s = s % ((R-1)*2)
    else:
        s = s % ((C-1)*2)

    
    sharks.append([r-1, c-1, s, d, z])

# 상어 사이즈가 작은 순서대로 정렬
sharks.sort(key = lambda x : x[4])

# =============== 디버깅용 출력 ===============

# def printBoard(board):
#     print(f"sharks : {sharks}\n")
#     for line in board:
#         for box in line:
#             print(f"{box}".ljust(14))
#         print("\n")
#     print("\n")
    
# def printCurr():
#     global sharks
#     newBoard = [[None for _ in range(C)] for _ in range(R)] # (idx, s, d, z) 형식으로 저장
#     for idx, (r, c, s, d, z) in enumerate(sharks):
#         newBoard[r][c] = (idx, s, d, z)
#     printBoard(newBoard)
        

# =============== 상어 이동 ===============
def move(dir, i, j, s):
    global R, C
    
    while s > 0:
        if dir == 1: # 위
            if i == 0:
                dir = 2
                continue
            i -= 1
        elif dir == 2: # 아래
            if i == R-1:
                dir = 1
                continue
            i += 1
        elif dir == 3: # 오른쪽
            if j == C-1:
                dir = 4
                continue
            j += 1
        else: # 왼쪽
            if j == 0:
                dir = 3
                continue
            j -= 1
        s -= 1
    return (dir, i, j)

def moveShark():
    global sharks, R, C

    newBoard = [[None for _ in range(C)] for _ in range(R)] # (idx, s, d, z) 형식으로 저장
    delSharks = []

    for idx, (r, c, s, d, z) in enumerate(sharks):
        newDir, newR,newC = move(d, r, c, s)

        if newBoard[newR][newC] != None: # 상어가 있는 경우

            # 기존 상어 삭제 해야하는 상어 목록에 추가
            # 상어 목록은 항상 사이즈가 작은것 부터 큰거 순으로 정렬되어 있기 때문
            delSharks.append(newBoard[newR][newC][0])

            # 새로운 상어로 변경
            newBoard[newR][newC] = (idx, s, d, z)
            sharks[idx][0] = newR
            sharks[idx][1] = newC
            sharks[idx][3] = newDir

        else: # 상어가 없는 경우
            newBoard[newR][newC] = (idx, s, d, z)
            sharks[idx][0] = newR
            sharks[idx][1] = newC
            sharks[idx][3] = newDir

    
    # 잡아먹힌 상어들 삭제
    for idx in sorted(delSharks, reverse=True):
        del sharks[idx]
        
    # printBoard(newBoard)

# =============== 상어 낚시 ===============
def fishing(curIdx):
    global sharks

    lineSharks = list(filter(lambda x : x[1][1] == curIdx, enumerate(sharks)))
    
    if not lineSharks:
        return 0

    delShark, idx = min(map(lambda x : (x[1], x[0]), lineSharks))
    del sharks[idx]
    # print(f"[DEBUG] fishing 결과 (+{delShark[4]})(delShark : {delShark}):\n")
    
    return delShark[4]
            

# =============== 상어 이동 ===============
# print("[DEBUG] 최초 바다 상황 : \n")
# printCurr()

result = 0
for time in range(C):
    # print(f"========== [DEBUG] {time + 1}초 \n")
    result += fishing(time)
    # printCurr()
    moveShark()
    

print(F"{result}")       