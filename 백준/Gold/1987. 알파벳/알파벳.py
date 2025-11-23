import sys

input = sys.stdin.readline
print = sys.stdout.write

R, C = map(int, input().rstrip().split())

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

# =========== DFS
is_visited = [[False for _ in range(C)] for _ in range(R)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_depth = 0

def dfs(x, y, depth, path):
    global R, C, max_depth, board
    is_visited[x][y] = True
    max_depth = max(depth, max_depth)

    for i, j in moves:
        nx = x + i
        ny = y + j

        if nx >= 0 and nx < R and ny >= 0 and ny < C and not is_visited[nx][ny]:
            if not( board[nx][ny] in path):
                dfs(nx, ny, depth + 1, path + board[nx][ny])
        
    is_visited[x][y] = False

dfs(0, 0, 1, board[0][0])
print(f"{max_depth}")
    

