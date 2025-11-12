import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

dp = [[-1 for _ in range(N)] for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i-1][0] + arr[i][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    
    result = dp[x2-1][y2-1]

    if x1 > 1:
        result -= dp[x1-2][y2-1]
    if y1 > 1:
        result -= dp[x2-1][y1-2]
    if x1 > 1 and y1 > 1:
        result += dp[x1-2][y1-2]
        
    print(F"{result}\n")