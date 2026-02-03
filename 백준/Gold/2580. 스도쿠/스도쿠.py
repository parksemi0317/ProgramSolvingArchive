import sys
from collections import deque

SIZE = 9
ALL = 0b111111111

input = sys.stdin.readline
print = sys.stdout.write

# ==================== 값 입력 받기 ====================

board = []

for _ in range(SIZE):
    board.append(list(map(int, input().rstrip().split())))


# ==================== 비트마스크 배열 만들기 ====================

bitMasks = [[0b0 for _ in range(SIZE)] for _ in range(SIZE)]
    

for i in range(SIZE):
    for j in range(SIZE):
        if board[i][j] != 0:
            mask = 0b1 << (board[i][j] -1)

            bitMasks[i][j] = ALL
            for idx in range(SIZE):
                bitMasks[i][idx]|= mask # 가로
                bitMasks[idx][j]|= mask # 세로
        
            # 정사각형
            startI = i // 3
            startJ = j // 3
            for iIdx in range(3):
                for jIdx in range(3):
                    bitMasks[3*startI + iIdx][3*startJ + jIdx] |= mask

# ======== 디버깅
# for line in board:
#     for n in line:
#         print(f"{n} ")
#     print("\n")

# ======== 디버깅
# print("\n======== 최초 bitMask 배열 ========\n")
# for line in bitMasks:
#     for mask in line:
#         print(f"{mask:09b} ")
#     print("\n")

# ==================== 큐 설정 & 재활용 함수 ====================

q = deque([])

# bitMask를 통해 확정 값인지 확인하는 함수
# 확정값이면 해당 값을, 확정 값이 없다면 -1을 반환
def isConfirmed(bitMask):
    curBitMask = bitMask ^ ALL

    for num in range(1, SIZE + 1):
        if curBitMask == (0b1 << num-1):
            return num
    return -1


# print(f"isConfirmed(0b111111110) : {isConfirmed(0b111111110)}\n")
# print(f"isConfirmed(0b111111111) : {isConfirmed(0b111111111)}\n")
# print(f"isConfirmed(0b111101111) : {isConfirmed(0b111101111)}\n")
# print(f"isConfirmed(0b011111111) : {isConfirmed(0b011111111)}\n")


# 비트 마스크 값 수정
def updateBitMask(num, i, j):
    global bitMasks, q, board

    bitMasks[i][j] |= (0b1 << (num-1))

    newNum = isConfirmed(bitMasks[i][j])
    if newNum != -1:
        board[i][j] = newNum # 확정여부 파악되면 바로 board 변경 (큐에 중복 삽입 막기 위함)
        bitMasks[i][j] = ALL
        q.append((newNum, i, j))

    
# ==================== 최초 확정 값 확인 ====================

# 초기 확정 값 큐에 삽입
for i in range(SIZE):
    for j in range(SIZE):

        num = isConfirmed(bitMasks[i][j])
        if num != -1:
            board[i][j] = num
            bitMasks[i][j] |= 0b1 << (num-1)
            q.append((num, i, j))

# ======== 디버깅
# print(f"\n======== 최초 q :\n")
# for qItem in q:
#     print(f"{qItem}\n")

# ==================== 확정 값들 처리 (큐에 들어가있는 목록들 처리) ====================

while q:
    num, i, j = q.popleft()
    
    mask = 0b1 << (num -1)

    for idx in range(SIZE):
        if board[i][idx] == 0: # 가로   
            updateBitMask(num, i, idx)
        if board[idx][j] == 0: # 세로
            updateBitMask(num, idx, j)

    # 정사각형
    startI = i // 3
    startJ = j // 3
    for iIdx in range(3):
        for jIdx in range(3):
            if board[3*startI + iIdx][3*startJ + jIdx] == 0:
                updateBitMask(num, 3*startI+iIdx, 3*startJ+jIdx)

# ======== 디버깅
# print("\n======== 확정 가능 값들 처리 후 board ========\n")
# for line in board:
#     for n in line:
#         print(f"{n} ")
#     print("\n")
# print("\n")

# ======== 디버깅
# print("\n======== 확정 가능 값들 처리 후 bitMask ========\n")
# for line in bitMasks:
#     for mask in line:
#         print(f"{mask:09b} ")
#     print("\n")

    
# ==================== 가능한 경우의 수 찾기 ====================

unknown = []
unknownCnt = 0

# 아직 답이 나오지 않은 값들 모으기
for i in range(SIZE):
    for j in range(SIZE):
        if board[i][j] == 0:
            unknown.append((i, j))
            unknownCnt += 1

# print(f"\nunknown ({len(unknown)}) : {unknown}\n\n")

# bitMask를 통해 가능한 값 목록 구하기
def getAbleNums(bitMask):
    result = []
    for num in range(1, SIZE+1):
        if bitMask & 0b1 == 0:
            result.append(num)
        bitMask = bitMask >> 1
        
    return result


    
def backTrack(idx):
    global bitMasks, unknownCnt, board
    # print(f"backTrack({idx})\n")

    if idx == unknownCnt:
        return 1 # 정답을 찾았다 (끝까지 도달)
    
    i, j = unknown[idx] # 현재 위치 값 찾기

    # 현재 위치에 가능한 값이 한개도 없는 경우
    if bitMasks[i][j] == ALL:
        return -1

    # 현재 위치에 가능한 값 목록 확인
    ableNums = getAbleNums(bitMasks[i][j])

    # 백트래킹 드가자
    flag = 0
    for num in ableNums:
        tmpMask = 0b1 << num-1
        
        board[i][j] = num
        bitMasks[i][j] |= tmpMask

        revertList = [] # 백트래킹을 위해 bitMask 변경한 위치 저장
        
        for k in range(SIZE):
            if bitMasks[i][k] & tmpMask == 0:
                revertList.append((i, k))
                bitMasks[i][k]|= tmpMask # 가로
            if bitMasks[k][j] & tmpMask == 0:
                revertList.append((k, j))
                bitMasks[k][j]|= tmpMask # 세로

        # 정사각형
        startI = i // 3
        startJ = j // 3
        for iIdx in range(3):
            for jIdx in range(3):
                if bitMasks[3*startI+iIdx][3*startJ+jIdx] & tmpMask == 0:
                    revertList.append((3*startI+iIdx, 3*startJ+jIdx))
                    bitMasks[3*startI + iIdx][3*startJ + jIdx] |= tmpMask
    
        # 다음탐색으로 넘어가기
        temp = backTrack(idx + 1)
        
        # 아니다. 돌아가자.
        if temp == -1:
            andMask = (0b1 << (num-1)) ^ ALL
            bitMasks[i][j] &= andMask

            for revI, revJ in revertList:
                bitMasks[revI][revJ] &= andMask

        # 정답을 찾았다. 더 찾을 필요 X
        if temp == 1:
            return 1

    return -1
        
                
backTrack(0)

for line in board:
    for n in line:
        print(f"{n} ")
    print("\n")
    