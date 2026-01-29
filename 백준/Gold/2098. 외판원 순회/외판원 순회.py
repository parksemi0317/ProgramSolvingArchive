import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# ==================== 값 입력 받기 ====================

N = int(input().rstrip())

bridges = []

for _ in range(N):
    bridges.append(list(map(int, input().rstrip().split())))

# ==================== DP 세팅 ====================

ALL_VISITED = (0b1 << N) -1
INF = 1000000 * 20

# [N][ALL_VISITED + 1]
# 마지막 위치, 전체 방문 여부
# INF : 미확인, -1 : 도달 불가
dp = [[INF for _ in range(ALL_VISITED+1)] for _ in range(N)]

# ===================== BFS ====================

q = deque([])

# 현재 위치에서 다시 원점으로 돌아가는데까지 남은 거리 반환 함수
# 돌아갈 수 없는 경우 -1 반환
def dfs(currentIdx, bitMask):
    global ALL_VISITED,INF, dp, bridges

    # 이미 값을 구한 경우 (Dp)
    if dp[currentIdx][bitMask] != INF:
        return dp[currentIdx][bitMask]
    
    if bitMask == ALL_VISITED:
        # 모든 경로를 전부 방문한 경우
        result = bridges[currentIdx][0] if bridges[currentIdx][0] else -1
        dp[currentIdx][bitMask] = result
        return result

    # 다음 경로로 이동하기
    result = INF
    for distIdx, dist in enumerate(bridges[currentIdx]):
        distBitMask = 0b1 << distIdx

        # 연결되어 있으며, 아직 방문하지 않은 경우
        if dist != 0 and bitMask & distBitMask == 0:
            newBitMask = bitMask | distBitMask

            nextDfs = dfs(distIdx, newBitMask)
            if nextDfs != -1:
                result = min(result, nextDfs + dist)

    if result == INF:
        result  = -1
    dp[currentIdx][bitMask] = result
    return result

print(f"{dfs(0, 0b1)}")
                



