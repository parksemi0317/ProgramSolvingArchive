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
            empts[(i+j)&0b1].append((i, j))

# print(f"[DEBUG] empts[0] : {empts[0]}\n")
# print(f"[DEBUG] empts[1] : {empts[1]}\n")

empty_white_len = len(empts[0])
empty_dark_len = len(empts[1])

# ======== DFS ========

# 비트 마스크 값 반환 함수
def get_bit_mask(i, j):
    if (i+j) &0b1: # 흑인 경우
        M1 = N-1
        m1 = ((i+j) // 2)
        
        M2 = (N // 2) * 2
        m2 = (i-j + M2 - 1) // 2
    
        mask1 = 0b1 << m1
        mask2 = (0b1 << M1) << m2
        
        return mask1 | mask2
        
    else:
        M1 = N
        m1 = ((i+j) // 2)
        
        M2 = N if N%2 else N-1
        m2 = (i-j + M2 - 1) // 2
    
        mask1 = 0b1 << m1
        mask2 = (0b1 << M1) << m2
        return mask1 | mask2

def get_max_cnt(empty_list):
    result = 0 # 결과 값 (최대 비숍 개수)
    empty_len = len(empty_list) # 빈 위치의 개수 (가지치기 및 끝 도달 확인용)
    
    def dfs(i, bitMask, cnt):
        nonlocal result, empty_len, empty_list
        
        if i == empty_len: # 끝에 도달한 경우
            result = max(cnt, result)
            return
    
        if empty_len - i + cnt <= result: # 가지치기
            return
    
        mask = get_bit_mask(empty_list[i][0], empty_list[i][1])    
        if mask & bitMask == 0b0:
            dfs(i+1, bitMask | mask , cnt + 1) # 놓는 경우
        
        dfs(i+1, bitMask , cnt) # 안놓는 경우
    
    dfs(0, 0b0, 0)
    return result

print(F"{get_max_cnt(empts[0]) + get_max_cnt(empts[1])}")