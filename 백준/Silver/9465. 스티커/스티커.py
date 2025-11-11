import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())

    stickers = []
    for i in range(2):
        stickers.append(list(map(int, input().rstrip().split())))


    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if n > 1:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]

    for y in range(2, n):
        dp[0][y] = max(dp[0][y-2], dp[1][y-2], dp[1][y-1]) + stickers[0][y]
        dp[1][y] = max(dp[1][y-2], dp[0][y-2], dp[0][y-1]) + stickers[1][y]

    print(f"{max(dp[0][-1],dp[1][-1])}\n")

        