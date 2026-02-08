import sys
INF = 10 ** 9

inputNums = list(map(int, input().split()))
stepCnt = len(inputNums) - 1
# print(stepCnt)

# dp[step][왼발 위치][오른발 위치] 
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(stepCnt+1)]

# 시작 위치
dp[0][0][0] = 0

def getMoveCost(start, to):
    if start == to:
        return 1
    if start == 0:
        return 2
    if start - to  == 1 or to - start == 1 or to - start == 3 or start - to == 3:
        return 3
    return 4

for step in range(1, stepCnt+1):
    to = inputNums[step-1]
    # print(f"========= step : {step} ({to}) =========")
    for left in range(5):
        for right in range(5):
            prevCost = dp[step-1][left][right]
            if prevCost < INF:

                if to != right:
                    # 왼쪽발 이동하기
                    dp[step][to][right] = min(dp[step][to][right], prevCost + getMoveCost(left, to))
                    # print(f"{left},{right} => {to},{right} : {dp[step][to][right]}")
                if to != left:
                    # 오른쪽 발 이동하기
                    dp[step][left][to] = min(dp[step][left][to], prevCost + getMoveCost(right, to))
                    # print(f"{left},{right} => {left},{to} : {dp[step][left][to]}")

print(min([dp[stepCnt][l][r] for l in range(5) for r in range(5)]))