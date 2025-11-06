import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# 입력값 받기
n,m = map(int, input().rstrip().split())

ground = [] # 땅 정보
goal = (-1, -1) # 목표 지점

# 목표지점으로부터 거리 정보
# 벽은 -2, 아직 도달하지 못한 곳은 -1
dp =[[-1 for _ in range(m)] for _ in range(n)]


for i in range(n):
    line = list(map(int, input().rstrip().split()))


    for j in range(m):
        if line[j] == 0:
            dp[i][j] = 0 # 벽은 0으로 세팅
        elif line[j] == 2:
            goal = (i, j)
            # print(f"[Debug] goal : {goal}\n")
            dp[i][j] = 0 # 종료지점은 0으로 세팅
    
    ground.append(line)

def print_dp():
    global dp
    
    for line in dp:
        for i in line:
            print(f"{i} ")
        print("\n")


can_visit_queue = deque([goal]) # 큐

while can_visit_queue:
    x,y = can_visit_queue.popleft()
    # print(F"\n\n[Debug] x : {x}, y : {y}\n")

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, j in moves:
        if x+i >=0 and x+i < n and y+j >=0 and y+j < m:
            if dp[x+i][y+j] == -1:
                dp[x+i][y+j] = dp[x][y] + 1
                can_visit_queue.append((x+i, y+j))
                # print(F"[Debug] x+i : {x+i}, y+j : {y+j}\n")
    
    # print(f"[Debug] can_visit_queue : {can_visit_queue}\n")

print_dp()


