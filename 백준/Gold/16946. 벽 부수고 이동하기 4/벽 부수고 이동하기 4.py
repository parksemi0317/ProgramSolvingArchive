import sys

input = sys.stdin.readline
print = sys.stdout.write

# ======== 값 입력 받기 ========

N, M = map(int, input().rstrip().split())

iMap = []
for _ in range(N):
    iMap.append(list(map(int, input().rstrip())))



# for line in iMap:
#     for c in line:
#         print(F"{c}".rjust(3))
#     print("\n")
# print("\n")

# ======== 분리집합 구하기 ========

parent = [[i * M + j if iMap[i][j] == 0 else -1 for j in range(M)] for i in range(N)]

# 디버깅용 출력 함수
def printParent():
    for line in parent:
        for c in line:
            print(F"{c}".rjust(3))
        print("\n")
    print("\n")

# 두 집합 합치는 함수
def join(i1, j1, i2, j2):

    root1 = getRoot(i1, j1)
    root2 = getRoot(i2, j2)

    if root1 < root2:
        parent[root2 // M][root2 % M] = root1
    else:
        parent[root1 // M][root1 % M] = root2

# 특정 위치의 부모 구하는 함수
def getRoot(i, j):
    newI, newJ = i , j
    while  newI*M + newJ != parent[newI][newJ]:
        newI, newJ = parent[newI][newJ] // M,  parent[newI][newJ] % M
    parent[i][j] = newI*M+newJ
    return newI*M+newJ

# print("초기 상태 : \n")
# printParent()

PREVS = [(0, -1), (-1, 0)]
for i in range(N):
    for j in range(M):
        
        if iMap[i][j] == 0: # 빈공간인 경우
            # print(f"[{i}],[{j}]\n")
            for mI, mJ in PREVS:

                if 0 <= i + mI < N and 0 <= j + mJ < M and iMap[i+mI][j+mJ] == 0 and parent[i][j] != parent[i+mI][j+mJ]:
                    join(i, j, i+mI, j+mJ)

# # ======== 각 집합별 수 구하기 ========

groupCnt = {}

for i in range(N):
    for j in range(M):

        if parent[i][j] > -1:
            getRoot(i, j)
            if parent[i][j] in groupCnt:
                groupCnt[parent[i][j]] += 1
            else:
                groupCnt[parent[i][j]] = 1

# print("최종 : \n")
# printParent()

# print(F"groupCnt : {groupCnt}\n")


# # ======== 출력하기 ========

ADJS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(N):
    for j in range(M):

        if iMap[i][j] == 0:
            print("0")
        else:
            groups = {}

            for mi, mj in ADJS:

                if 0 <= i + mi < N and 0 <= j + mj < M and iMap[i+mi][j+mj] == 0:
                    groups[parent[i+mi][j+mj]]= True

            print(f"{(sum([groupCnt[key] for key in groups]) + 1)% 10}")
    print("\n")           