import sys
from copy import deepcopy

input = sys.stdin.readline
print = sys.stdout.write

# ======== 값 입력 받기 ========

N = int(input().rstrip())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# ======== 빈 공간들만 추출 ========

empts = [[], []] # [i + j 가 짝수인 공간 (백)], [i + j 가 홀수인 공간 (흑)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: # 비어 있는 경우
            empts[(i+j)%2].append((i, j))

# print(f"[DEBUG] empts[0] : {empts[0]}\n")
# print(f"[DEBUG] empts[1] : {empts[1]}\n")

empty_white_len = len(empts[0])
empty_dark_len = len(empts[1])

# ======== 백 (짝수) DFS ========

def get_white_bitmask(i, j):
    M1 = N
    m1 = ((i+j) // 2)
    
    M2 = N if N%2 else N-1
    m2 = (i-j + M2 - 1) // 2

    mask1 = 0b1 << m1
    mask2 = (0b1 << M1) << m2
    
    return mask1 | mask2

white_max = 0
def dfs_white(i, bitMask, cnt):
    global white_max
    
    # 끝에 도달한 경우
    if i == empty_white_len:
        white_max = max(cnt, white_max)
        return

    # 가지치기
    if empty_white_len - i + cnt <= white_max:
        return

    # 놓을 수 있는 경우
    mask = get_white_bitmask(empts[0][i][0], empts[0][i][1])
    if mask & bitMask == 0b0:
        dfs_white(i+1, bitMask | mask , cnt + 1)
    
    dfs_white(i+1, bitMask , cnt)

# print(f"[DEBUG] get_white_bitmask(0, 0) : {get_white_bitmask(0, 0):b}\n")
# print(f"[DEBUG] get_white_bitmask(2, 2) : {get_white_bitmask(2, 2):b}\n")
# print(f"[DEBUG] get_white_bitmask(3, 1) : {get_white_bitmask(3, 1):b}\n")


dfs_white(0, 0b0, 0)
# print(f"white_max : {white_max}\n")
# ======== 흑 (짝수) DFS ========

def get_black_bitmask(i, j):
    M1 = N-1
    m1 = ((i+j) // 2)
    
    M2 = (N // 2) * 2
    m2 = (i-j + M2 - 1) // 2

    mask1 = 0b1 << m1
    mask2 = (0b1 << M1) << m2
    
    return mask1 | mask2

black_max = 0
def dfs_black(i, bitMask, cnt):
    global black_max
    
    # 끝에 도달한 경우
    if i == empty_dark_len:
        black_max = max(cnt, black_max)
        return

    # 가지치기
    if empty_dark_len - i + cnt <= black_max:
        return

    # 놓을 수 있는 경우
    mask = get_black_bitmask(empts[1][i][0], empts[1][i][1])
    if mask & bitMask == 0b0:
        dfs_black(i+1, bitMask | mask , cnt + 1)
    
    dfs_black(i+1, bitMask , cnt)

dfs_black(0, 0b0, 0)
# print(f"black_max : {black_max}")
print(f"{black_max + white_max}")