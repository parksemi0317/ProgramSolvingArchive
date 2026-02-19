import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

# ============= 값 입력 받기 =============

m, n = map(int, input().rstrip().split())

board = []
for _ in range(m):
    board.append(list(map(int, input().rstrip().split())))

# ============= 디버깅 =============

def printMatrix(board):
    for line in board:
        for c in line:
            print(F"{c} ")
        print("\n")
    print("\n")

# printMatrix(board)
# ============= dp =============

q = [(-board[0][0], 0, 0)]
adjacent = ((0, 1), (0, -1), (1, 0), (-1, 0))

dp = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
dp[0][0] = 1
visited[0][0] = True

while q:
    num, i, j = heapq.heappop(q)
    num = -num

    for x, y in adjacent:
        if 0 <= i + x  and i+x < m and 0 <= j + y and j+y < n:
            if board[i+x][j+y] < num:
                dp[i+x][j+y] += dp[i][j]

                if not visited[i+x][j+y]:
                    heapq.heappush(q, (-board[i+x][j+y], i+x, j+y))
                    visited[i+x][j+y] = True

# printMatrix(dp)  
print(f"{dp[m-1][n-1]}")
