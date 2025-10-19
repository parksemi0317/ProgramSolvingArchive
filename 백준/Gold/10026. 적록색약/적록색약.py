import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

# ========= 입력 값 입력 받기 =========

# N 입력 받기
N = int(input().rstrip())

painting = [] # 그림 이차원 배열
# 그림 정보 입력 받기
for _ in range(N):
    painting.append(list(input().rstrip()))


group_arr = [[0 for i in range(N)] for j in range(N)] # 그룹 정보 배열
# ========= 깊이 우선 탐색 코드 =========

def search(color , x, y, team_idx):
    global painting, N, group_arr

    group_arr[x][y] = team_idx
    # print(f"\n[Debug] search({color}, {x}, {y}, {team_idx})\n")
    # print_group_for_debug()

    if x > 0 and painting[x-1][y] == color and group_arr[x-1][y] == 0:
        search(color, x-1, y, team_idx)
    if x < N-1 and painting[x+1][y] == color and group_arr[x+1][y] == 0:
        search(color, x+1, y, team_idx)
    if y > 0 and painting[x][y-1] == color and group_arr[x][y-1] == 0:
        search(color, x, y-1, team_idx)
    if y < N-1 and painting[x][y+1] == color and group_arr[x][y+1] == 0:
        search(color, x, y+1, team_idx)
        
# ========= 적록색맹이 아닌 사람의 경우 =========

# print("[Debug] 적록 생맹이 아닌 사람의 경우 : \n")
# print_painting_for_debug()

team_cnt = 0

for x, line in enumerate(painting):
    for y, pixel in enumerate(line):
        if group_arr[x][y] == 0:
            team_cnt += 1
            search(pixel, x, y, team_cnt)

# print_group_for_debug()
print(f"{team_cnt}")


# ========= 적록색맹인 사람의 경우 =========

group_arr = [[0 for i in range(N)] for j in range(N)]

painting = [["R" if pixel != "B" else "B" for pixel in line] for line in painting]    

# print("\n[Debug] 적록 생맹인 사람의 경우 : \n")
# print_painting_for_debug()

team_cnt = 0
for x, line in enumerate(painting):
    for y, pixel in enumerate(line):
        if group_arr[x][y] == 0:
            team_cnt += 1
            search(pixel, x, y, team_cnt)

# print_group_for_debug()
print(f" {team_cnt}")
  
        