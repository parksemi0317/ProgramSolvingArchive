import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# ============= N, M, K, 사탕 수 입력 받기 =============
N, M, K = map(int, input().rstrip().split())
candy = list(map(int, input().rstrip().split()))

# ============= 친구 그룹 묶기 (disjointSet) =============
childGroups = [i+1 for i in range(N)]

def findRoot(childNum):
    global childGroups

    if childNum == childGroups[childNum-1]:
        return childNum
    root = findRoot(childGroups[childNum-1]) # 재귀로 평탄화
    childGroups[childNum-1] = root
    return root

for _ in range(M):
    a, b = map(int, input().rstrip().split())

    aRoot = findRoot(a)
    bRoot = findRoot(b)
    if aRoot < bRoot:
        childGroups[bRoot-1] = aRoot
    else:
        childGroups[aRoot-1] = bRoot

# print(f"[DEBUG] childGroups : {childGroups}\n")

# ============= 친구 그룹 정리 =============

group = {} # 대표 아이 번호 : [그룹 인원수, 전체 사탕 총 합] 형식으로 저장

for childIdx in range(N):

    root = findRoot(childIdx+1)
    if root in group:
        group[root][0] += 1
        group[root][1] += candy[childIdx]
    else:
        group[root] = [1, candy[childIdx]]

# print(f"[DEBUG] group : {group}\n")

# ============= 내부 인원수별로 다시 묶기 =============

childCntGroup = {} # 인원수 : 전체 사탕 총합 배열 형식으로 저장
childCntCnt = 0

for groupKey in group:
    if group[groupKey][0] in childCntGroup:
        childCntGroup[group[groupKey][0]].append(group[groupKey][1])
    else:
        childCntGroup[group[groupKey][0]] = [group[groupKey][1]]
        childCntCnt += 1

# 내림차순 정렬
for childCnt in childCntGroup:
    childCntGroup[childCnt].sort(reverse=True)

# print(f"[DEBUG] childCntGroup : {childCntGroup}\n")
# print(f"[DEBUG] childCntCnt : {childCntCnt}\n")

# ============= dp =============

# [마지막 childCnt idx][현재 울린 아이들 수]
dp = [[0 if i==0 else -1 for i in range(K)] for _ in range(childCntCnt+1)]

result = 0
for i, childCnt in enumerate(childCntGroup):
    
    # print(F"\n======== [DEBUG] i : {i}, childCnt : {childCnt} {childCntGroup[childCnt]}\n")

    curGroupChildSum = 0
    curGroupCandy = 0
    for newGroupCandy in childCntGroup[childCnt]:
        curGroupChildSum += childCnt # 현재 그룹에서 더하려고 하는 아이들 수
        curGroupCandy += newGroupCandy
        
        for prevChidCnt in range(K-curGroupChildSum):
            for prevIdx in range(i+1):
                if dp[prevIdx][prevChidCnt] != -1:
                    dp[i+1][prevChidCnt + curGroupChildSum] = max(dp[i+1][prevChidCnt + curGroupChildSum], dp[prevIdx][prevChidCnt] + curGroupCandy)
                    result = max(result, dp[i+1][prevChidCnt + curGroupChildSum])
                    # print(F"[DEBUG] dp[{i+1}][{prevChidCnt +curGroupChildSum}] : {dp[i+1][prevChidCnt + curGroupChildSum]}\n")

print(F"{result}")