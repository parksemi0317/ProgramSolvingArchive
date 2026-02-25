import sys
import copy
INF = 10 ** 9

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

A = list(map(int, input().rstrip().split()))
W = list(map(int, input().rstrip().split()))


# dp[현재 매모리] = 비활성화 비용 (작을수록 좋음)
dp = [INF for _ in range(M+1)]
dp[0] = 0

for step in range(N):
    
    curA = A[step]
    curW = W[step]

    for i in range(M, -1, -1):
        if dp[i] < INF:
            if i + curA < M:
                dp[i + curA] =  min(dp[i+curA], dp[i] + curW)
            else:
                dp[M] = min(dp[M], dp[i] + curW)
print(F"{dp[M]}")  