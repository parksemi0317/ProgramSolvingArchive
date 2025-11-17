import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
M = int(input().rstrip())

INF = 100001 * M

# print(f"[DEBUG] N : {N}, M : {M}\n")

# =============== 버스 정보 입력 받기

bus = {}

for i in range(1, N+1):
    bus[i] = []

for _ in range(M):
    s, e, c = map(int, input().rstrip().split())
    bus[s].append((e, c))

# print(f"[DEBUG] bus : {bus}\n")


# =============== 시작 위치, 종료 위치 입력 받기

S, E = map(int, input().rstrip().split())

# =============== 다익스트라 알고리즘

dp = [INF for _ in range(N)]
dp[S-1] = 0
isVisited = [0 for _ in range(N)]

# 다음으로 방문할 노드 탐색
def findNextNodeIdx():
    global dp, isVisited
    # print(f"[DEBUG] isVisited : {isVisited}\n")
    result = -1
    for i in range(N):
        if dp[i] != INF and isVisited[i] == 0:
            if result == -1 or dp[i] < dp[result]:
                result = i
    if result != -1:
        isVisited[result] = 1
    return result
    
cnt = 0
nextIdx = findNextNodeIdx()
while cnt < N and nextIdx != -1:
    # print(f"[DEBUG] {nextIdx+1} 노드 방문\n")
    for e, c in bus[nextIdx+1]:
        dp[e-1] = min(dp[e-1] , dp[nextIdx] + c)
    # print(F"dp : {dp}\n\n")
    nextIdx = findNextNodeIdx()

# print(F"dp : {dp}\n")
print(f"{dp[E-1]}")

