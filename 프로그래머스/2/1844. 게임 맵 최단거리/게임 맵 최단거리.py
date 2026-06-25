from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # print("n, m :",n, m)
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque([(0, 0, 1)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while q:
        x,y,move = q.popleft()
        if x == n-1 and y == m-1:
            return move
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny, move + 1))
                visited[nx][ny] = True
    return -1
        
        
        
        