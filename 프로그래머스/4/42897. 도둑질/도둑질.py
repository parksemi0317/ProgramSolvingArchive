
def solution(money):
    n = len(money)
    dp = [[[0 for _ in range(2)]for _ in range(n)] for _ in range(2) ]
    
    # dp [시작집 포함여부][종료집 idx][종료집 포함 여부]
    dp[1][0][1] = money[0]
    dp[0][0][0] = 0
    
    for endIdx in range(1, n):
        dp[1][endIdx][1] = dp[1][endIdx-1][0] + money[endIdx]
        dp[1][endIdx][0] = max(dp[1][endIdx-1][0], dp[1][endIdx-1][1])
        
        dp[0][endIdx][1] = dp[0][endIdx-1][0] + money[endIdx]
        dp[0][endIdx][0] = max(dp[0][endIdx-1][0], dp[0][endIdx-1][1])
    return max(dp[0][n-1][1], dp[1][n-1][0], dp[0][n-1][0])