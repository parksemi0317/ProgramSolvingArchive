import sys

input = sys.stdin.readline
print = sys.stdout.write


# ============== 값 입력 받기

N, L = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# ============== 

def checkIsLoad(arr):
    global N, L

    idx = 1
    startIdx = 0 # 현재와 동일한 높이가 언제부터 시작되었는지 확인 (경사로 설치구역 제외)
    needSlope = False
    
    while idx < N:
        # CASE 1: 이전 값과 동일한 경우
        if arr[idx] == arr[idx-1]:
            if needSlope and idx - startIdx + 1 == L: # 경사로 설치가 끝난 경우
                    needSlope = False
                    startIdx = idx + 1

        # CASE 2: 한칸 밑으로 내려온 경우
        elif arr[idx-1] - arr[idx] == 1:
            if needSlope: # 경사로 설치를 했어야 하는 경우
                # print(F" idx {idx} case2 \n")
                return False

            if L == 1: # 바로 경사로 설치 가능
                startIdx = idx + 1
            else:
                needSlope = True # 경사로를 설치해야함
                startIdx = idx

        # CASE 3: 한칸 위로 올라온 경우
        elif arr[idx] - arr[idx-1] == 1:
            if needSlope: # 경사로 설치를 했어야 하는 경우
                # print(F" idx {idx} case3-1 \n")
                return False

            if idx - startIdx < L: # 앞에 경사로 설치가 불가능한 경우
                # print(F" idx {idx} case3-2 \n")
                return False
            
            startIdx = idx
        
        else: # 한칸 이상 차이나는 경우
            # print(F" idx {idx} case4 \n")
            return False
        idx += 1

    if needSlope:
        # print(F" case5 \n")
        return False
    return True
        
# ============== 
result = 0

for i in range(N):
    # print(F"[DEBUG] idx {i} 가로 길")
    if checkIsLoad(board[i]): # 가로 확인
        # print(F" 존재\n")
        result += 1
    # print(F"[DEBUG] idx {i} 세로 길")
    if checkIsLoad([board[j][i] for j in range(N)]):
        # print(F" 존재\n")
        result += 1


print(F"{result}")
    