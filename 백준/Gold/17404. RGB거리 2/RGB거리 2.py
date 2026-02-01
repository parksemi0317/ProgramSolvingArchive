import sys
INF = 10 ** 9

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
# dp[시작 색상][현재 위치][현재 색상]
dp = [[[INF, INF, INF] for i in range(N)] for _ in range(3)]

# ================== 첫번째 값 ==================

# 첫번째 값 입력 받기
colors = list(map(int, input().rstrip().split()))

# 첫번째 값 처리
for colorIdx in range(3):
    dp[colorIdx][0][colorIdx] = colors[colorIdx]

# ================== 중간 값 ==================

# 중간 값 입력 받기 & 처리
for i in range(N-1):
    colors = list(map(int, input().rstrip().split()))

    for lastColorIdx in range(3):
        for startColorIdx in range(3): 
            dp[startColorIdx][i+1][lastColorIdx] = min(dp[startColorIdx][i][(lastColorIdx + 1) % 3], dp[startColorIdx][i][(lastColorIdx + 2) % 3]) + colors[lastColorIdx] 

# ================== 디버깅용 출력 ==================

# for idx, colors in enumerate(dp):
#     print(f"\n시작색상 : {idx} \n")
#     for line in colors:
#         for num in line:
#             print(f"{num if num < INF else "INF"}".rjust(5))
#         print("\n")

# ================== 시작 색상과 종료 색상이 다른 경우들 중 최솟값 찾기 ==================
result = INF
for startColorIdx in range(3):
    result = min(result, dp[startColorIdx][N-1][(startColorIdx+1)%3], dp[startColorIdx][N-1][(startColorIdx+2)%3])

print(F"{result}")