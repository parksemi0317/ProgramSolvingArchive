import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

'''
====================
    그룹 구하는 함수 모음
====================
''' 

def normalize(group):
    group.sort()
    sX, sY = group[0]
    for i in range(len(group)):
        group[i][0] -= sX
        group[i][1] -= sY
    return group
    

def dfs(n, game_board,visited, x, y, target, neighbors):
    neighbors.append([x, y])
    visited[x][y] = True
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and game_board[nx][ny] == target:
            dfs(n, game_board,visited, nx, ny, target, neighbors)


def getGroups(board_size, board, target):
    global answer
    tmp_visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    groups = []
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == target and not tmp_visited[i][j]:
                new_group = []
                dfs(board_size,board, tmp_visited, i, j, target, new_group)
                groups.append(new_group)
                
    return groups

'''
====================
    block 돌리는 함수
====================
''' 

def rotate(block):
    for i in range(len(block)):
        block[i] = [-block[i][1], block[i][0]]
    return block

'''
====================
    같은지 비교 함수
====================
''' 

def isSame(block, blank):
    block_len = len(block)
    
    for i in range(block_len):
        if block[i][0] == blank[i][0] and block[i][1] == blank[i][1]:
            continue
        return False
    return True

'''
====================
    solution 
====================
''' 

def canFillBlank(blank, block_group_cnt,used, block_groups, rotated_group):
    for block_idx in range(block_group_cnt): # 블록에 대하여 반복문 실행
        if used[block_idx]: # 블록이 아직 사용되지 않은 경우에 대해서만 확인
                continue
            
        block_len = len(block_groups[block_idx])
        blank_len = len(blank)
        if block_len != blank_len: # 길이가 같은 경우에 대해서만 확인
            continue
                
        for block in rotated_group[block_idx]: # 네가지 회전 상황에 대하여 처리
            if isSame(block, blank):
                
                used[block_idx] = 1
                return len(block)
    return 0

def solution(game_board, table):
    board_size = len(game_board)
    # ====== game_board의 공백 그룹 구하기    
    blank_groups = getGroups(board_size, game_board, 0)
    blank_group_cnt = len(blank_groups)
    for group in blank_groups:
        normalize(group)
    
    # ====== table의 블록 그룹 구하기
    
    block_groups = getGroups(board_size, table, 1)
    block_group_cnt = len(block_groups)
    
    # ====== table의 블록 그룹 회전 정보 구하기
    rotated_group = []
    for group in block_groups:
        normalize(group)
        tmp = [group[:]]
        for i in range(3):
            rotate(group)
            normalize(group)
            tmp.append(group[:])
        rotated_group.append(tmp)

    
    # ====== 비교
    result = 0
    used = [False] * block_group_cnt
    for blank in blank_groups: # 공백에 대하여 반복문 실행
        result += canFillBlank(blank, block_group_cnt,used, block_groups, rotated_group)
    return result
    