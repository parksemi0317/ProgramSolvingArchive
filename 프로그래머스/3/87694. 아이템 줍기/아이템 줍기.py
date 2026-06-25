from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 2배 확대를 위해 102x102 크기 보드 생성
    board = [[-1] * 102 for _ in range(102)]
    
    # 2. 사각형 채우기 (테두리는 1, 내부는 0, 빈 공간은 -1)
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 다른 사각형의 '내부(0)'가 아닌 경우에만 채우기
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0: 
                    board[i][j] = 1

    # 3. BFS를 위한 설정 (시작점, 도착점도 2배 확대)
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(cx, cy)])
    # 방문 여부 및 거리를 기록할 배열 (시작점 거리를 1로 설정)
    visited = [[0] * 102 for _ in range(102)]
    visited[cx][cy] = 1
    
    # 4. BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        
        # 아이템을 찾으면 현재까지의 거리 반환 (시작을 1로 했으므로 딱 맞음)
        if x == ix and y == iy:
            return visited[x][y] // 2 # 2배 확대했으므로 다시 2로 나눔
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 범위 안이고, 테두리(1)이며, 아직 방문하지 않은 곳이라면
            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return 0