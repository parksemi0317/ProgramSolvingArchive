import sys

input = sys.stdin.readline
print = sys.stdout.write

# =========== 값 입력 받기 ===========

N, M = map(int, input().rstrip().split())

inputMap = []

for _ in range(N):
    inputMap.append(list(input().rstrip()))

# for line in inputMap:
#     print(F"{line}\n")

# =========== 탐색 함수 ===========

groupCount = 0
groupMap = [[-1 for _ in range(M)] for _ in range(N)]

def search(curI, curJ, prevs):
    global groupCount, groupMap, inputMap

    # 이전에 발견한 사이클에 도달한 경우
    if groupMap[curI][curJ] != -1:
        for i, j in prevs:
            groupMap[i][j] = groupMap[curI][curJ]
    # 사이클 발견한 경우
    elif (curI, curJ) in prevs:
        groupCount += 1
        for i, j in prevs:
            groupMap[i][j] = groupCount
    else:
        if inputMap[curI][curJ] == "D":
            search(curI+1, curJ, prevs + [(curI, curJ)])
        elif inputMap[curI][curJ] == "U":
            search(curI-1, curJ, prevs + [(curI, curJ)])
        elif inputMap[curI][curJ] == "L":
            search(curI, curJ-1, prevs + [(curI, curJ)])
        elif inputMap[curI][curJ] == "R":
            search(curI, curJ+1, prevs + [(curI, curJ)])

# =========== 그룹이 없는 경우 탐색 ===========

for i in range(N):
    for j in range(M):
        if groupMap[i][j] == -1:
            search(i, j, [])

print(F"{groupCount}")
            
            