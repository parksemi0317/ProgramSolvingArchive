import sys
from collections import deque
sys.setrecursionlimit(10 ** 4)

MOVES = ((1, 0), (-1, 0), (0, 1), (0, -1))
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    # print("\n")
    result = 0
    # ================== 값 입력 받기 ================== 
    h, w = map(int, input().rstrip().split())

    buildingMap = [list(input().rstrip()) for _ in range(h)]

    # for line in buildingMap:
    #     print(line)

    keys = list(input().rstrip())

    # ================== 가지고 있는 key 정보 가공 ==================
    
    hasKey = [False for _ in range(26)]
    orda = ord('a')
    ordA = ord('A')
    
    if keys[0] != "0":
        for k in keys:
            hasKey[ord(k) - orda] = True
    # print("hasKey :", hasKey)

    # ================== 공통 유틸 함수 ==================

    q = deque([])
    unOpendedDoors = [[] for _ in range(26)]

    # 특정 위치로 이동할 수 있는지 확인하는 함수
    def canMove(i, j):
        if buildingMap[i][j] == "*": # 벽이 위치해 있는 경우
            return False
        if 'A' <= buildingMap[i][j] <= 'Z': # 문이 위치해 있는 경우
            idx = ord(buildingMap[i][j]) - ordA
            
            if hasKey[idx]: # 해당 키를 가지고 있는 경우
                return True
            # 해당 키를 가지고 있지 않은 경우 열지 못한 문 목록에 추가
            unOpendedDoors[idx].append((i, j))
            # print(f"[DEBUG] 열지 못한 {buildingMap[i][j]}문 {(i, j)} 추가")
            return False
        
        return True # 문서가 있거나, 열쇠가 있거나, 빈 공간인 경우

    # ================== 빌딩 진입 지점 찾기 ==================
    # 상, 하
    for i in range(w):
        if canMove(0, i): 
            q.append((0, i))
        if canMove(h-1, i):
            q.append((h-1, i))
    # 좌, 우
    for i in range(h):
        if canMove(i, 0):
            q.append((i, 0))
        if canMove(i, w-1):
            q.append((i, w-1))

    # print(f"[DEBUG] 최초 진입 가능 지점 :", q)
    
    # ================== 빌딩 내부 탐색  ==================
    hasVisited = [[False for _ in range(w)] for _ in range(h)]

    def dfs(i, j):
        global result
        if buildingMap[i][j] == "$": # 문서를 찾은 경우
            # print(f"[DEBUG] {i}, {j}에서 문서 발견")
            result += 1
        elif 'a' <= buildingMap[i][j] <= 'z': # 열쇠를 찾은 경우
            # print(f"[DEBUG] {i}, {j}에서 {buildingMap[i][j]} 열쇠 발견")
            idx= ord(buildingMap[i][j]) -orda
            hasKey[idx] = True
            # 이미 발견한 문들 큐에 삽입추가
            for door in unOpendedDoors[idx]:
                # print(f"[DEBUG] {buildingMap[i][j]}문 {door} 큐에 삽입")
                q.append(door)
            unOpendedDoors[idx] = []
        
        hasVisited[i][j] = True
        
        # 상하 좌우로 이동하기 (dfs)
        for mI, mJ in MOVES:
            if 0 <= i+mI < h and 0 <= j+mJ < w and not hasVisited[i+mI][j+mJ] and canMove(i+mI, j+mJ):
                dfs(i+mI, j+mJ)
                
    
    while q:
        spI, spJ = q.popleft()

        if not hasVisited[spI][spJ]:
            # print(f"\n[DEBUG] {spI}, {spJ}부터 탐색 시작")
            dfs(spI, spJ)

    print(result)
    