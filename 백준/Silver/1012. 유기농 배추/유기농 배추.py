import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

field = []
N = M = K = 0

def search_bfs(x, y):
    global field, N, M

    field[x][y] = -1

    if x > 0 and field[x-1][y] == 1:
        search_bfs(x-1, y)
    if x < N-1 and field[x+1][y] == 1:
        search_bfs(x+1, y)
    if y > 0 and field[x][y-1] == 1:
        search_bfs(x, y-1)
    if y < M-1 and field[x][y+1] == 1:
        search_bfs(x, y+1)

for _ in range(T):

    N, M, K = list(map(int, input().rstrip().split()))
    
    
    field = [[0 for _ in range(M)] for _ in range(N)]

    
    for _ in range(K):
        x, y = map(int, input().rstrip().split())
        field[x][y] = 1

    result = 0
    for x in range(N):
        for y in range(M):
            if field[x][y] == 1:
                result += 1
                search_bfs(x, y)

    print(f"{result}\n")