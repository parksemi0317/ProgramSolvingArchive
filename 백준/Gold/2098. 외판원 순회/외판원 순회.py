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
dp = [[INF for _ in range(ALL_VISITED+1)] for _ in range(N)]

# ==================== 탐색 함수 ====================

q = deque([])

# 1에서 이동 가능한 지점들 표시
for idx, dist in enumerate(bridges[0]):
    if dist != 0:
        bitMask = 0b1 << idx
        dp[idx][bitMask] = dist
        q.append((idx, bitMask))


while q:
    currentIdx , bitMask = q.popleft()
    curDistance = dp[currentIdx][bitMask]
    
    for distIdx, dist in enumerate(bridges[currentIdx]):
        distBitMask = 0b1 << distIdx

        # 연결되어 있으며, 아직 방문하지 않은 경우
        if dist != 0 and bitMask & distBitMask == 0:
            newBitMask = bitMask | distBitMask
            
            if curDistance + dist < dp[distIdx][newBitMask]:
                dp[distIdx][bitMask | distBitMask] = curDistance + dist
                q.append((distIdx, bitMask | distBitMask))

print(f"{dp[0][ALL_VISITED]}")
                



