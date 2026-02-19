import sys

input = sys.stdin.readline
print = sys.stdout.write

# ============= 값 입력 받기 =============

n, k = map(int, input().rstrip().split())

coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))
# print(f"coins : {coins}\n")
    
# ============= DP =============

# dp[i번째 동전까지 사용][금액] : 가능한 경우의 수

dp = [0 for j in range(k+1)]
dp[0] = 1

for coin in coins:
    for money in range(coin, k+1):
        dp[money] += dp[money-coin]
print(F"{dp[k]}")