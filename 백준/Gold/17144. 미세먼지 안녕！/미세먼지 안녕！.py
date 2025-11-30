import sys
import copy

input = sys.stdin.readline
print = sys.stdout.write

## ================= 입력 값 받기
R, C, T = map(int, input().rstrip().split())

room = []

for _ in range(R):
    room.append(list(map(int, input().rstrip().split())))

## ================= 확산
    
MOVES = ((0, 1), (0, -1), (1, 0), (-1, 0))

def spread(room):
    global R, C
    prevRoom = copy.deepcopy(room)

    
    for i in range(R):
        for j in range(C):
            if prevRoom[i][j] > 0:
                spread = []
                cnt = 0
                # 확산 가능 칸 및 칸수 찾기
                for mi, mj in MOVES:
                    if i + mi >=0 and i + mi < R and j + mj >= 0 and j + mj < C and prevRoom[i+mi][j+mj]!= -1:
                        spread.append((i+mi, j+mj))
                        cnt += 1

                # 확산
                for x, y in spread:
                    room[x][y] += prevRoom[i][j] // 5
                room[i][j] -= cnt * (prevRoom[i][j] // 5)            

## ================= 공기 청정기 작동

# 공기청정기 위치 찾기
refresher = 0
for i in range(R):
    if room[i][0] == -1:
        refresher = i
        break

def refresh(room):
    global refresher, R, C

    # ===== 위쪽 공기청정기 작동
    # 좌측 하단 이동
    for i in range(refresher-2, -1, -1):
        room[i+1][0] = room[i][0]
    # 상단 좌측 이동
    for j in range(1, C):
        room[0][j-1] = room[0][j]
    # 우측 상단 이동
    for i in range(1, refresher+1):
        room[i-1][C-1] = room[i][C-1]
    # 하단 우측 이동
    for j in range(C-2,0 , -1):
        room[refresher][j+1] = room[refresher][j]
    room[refresher][1] = 0

    # ===== 아래쪽 공기청정기 작동
    # 좌측 상단 이동
    for i in range(refresher+3, R):
        room[i-1][0] = room[i][0]
    # 하단 좌측 이동
    for j in range(1, C):
        room[R-1][j-1] = room[R-1][j]
    # 우측 하단 이동
    for i in range(R-2, refresher, -1):
        room[i+1][C-1] = room[i][C-1]
    # 상단 우측 이동
    for j in range(C-2,0 , -1):
        room[refresher+1][j+1] = room[refresher+1][j]
    room[refresher+1][1] = 0
        
    
        

## ================= 디버깅용 출력 함수           


def printRoom(room):
    for line in room:
        for c in line:
            print(f"{c}".rjust(3))
        print("\n")
# printRoom(room)


for time in range(T):
    # print(f"\n\n============ [DEBUG] time : {time} ============")

    spread(room)
    # print(f"\n[DEBUG] 확산 완료\n")
    #printRoom(room)
    
    refresh(room)
    # print(f"\n[DEBUG] 정화 완료\n")
    # printRoom(room)

print(f"{sum([sum(room[i]) for i in range(R)]) + 2}")

    