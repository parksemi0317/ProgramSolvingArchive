N = int(input())
buildings = list(enumerate(map(int, input().split()))) # (idx, 높이)

# print("[DEBUG] buildings :", buildings)

leftDp = [[0, -1] for _ in range(N)] # (좌측에 보이는 빌딩 수, 가장 가까이 보이는 좌측 건물 idx)
rightDp = [[0, -1] for _ in range(N)] # (우측에 보이는 빌딩 수, 가장 가까이 보이는 우측 건물 idx)

# buildings 배열을 받아 왼쪽부터 순회하면서 좌측에 보이는 빌딩 수와 가장 가까이 보이는 빌딩 인덱스 저장
def getLeftDp(buildings, dp):
    for i in range(1, N):
        
        if buildings[i-1][1] > buildings[i][1]: # 좌측 빌딩이 더 큰 경우
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = buildings[i-1][0] # 좌측 빌딩이 가장 먼저 보임
        elif buildings[i-1][1] == buildings[i][1]: # 좌측 빌딩과 같은 경우
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1] # 좌측에 보이는 빌딩은 동일
        else: # buildings[i-1][1] < buildings[i][1]
            j = i-1
            while j >= 0 and buildings[j][1] < buildings[i][1]:
                j -= 1
            if j < 0:
                continue

            if buildings[j][1] == buildings[i][1]:
                dp[i][0] = dp[j][0]
                dp[i][1] = dp[j][1]
            else:
                dp[i][0] = dp[j][0]+1
                dp[i][1] = buildings[j][0]
            
# ========== 1. 좌측 빌딩 확인
getLeftDp(buildings, leftDp)
# print("[DEBUG] leftDp    :", leftDp)

# ========== 2. 우측 빌딩 확인
buildings.reverse()
getLeftDp(buildings, rightDp)
# print("[DEBUG] rightDp   :", rightDp)
rightDp.reverse()
# print("[DEBUG] rightDp   :", rightDp)

# ========== 3. 좌측과 우측 합쳐서 결과 출력

# 좌축과 우측에 보이는 인덱스 받아서 출력해야하는 빌딩 번호 반환
def getNearst(left, right, i):
    if left == -1:
        return right + 1
    elif right == -1:
        return left + 1
    elif (i-left) > (right-i):
        return right + 1
    elif (i-left) <= (right-i):
        return left + 1
        
for i in range(N):
    cnt = leftDp[i][0] + rightDp[i][0]
    if cnt != 0:
        print(cnt, getNearst(leftDp[i][1], rightDp[i][1], i))
    else:
        print(cnt)