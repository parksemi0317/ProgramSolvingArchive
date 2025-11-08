import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
dp = []

for i in range(n):
    dp.append(list(map(int, input().rstrip().split())))


for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
        
print(f"{dp[0][0]}")