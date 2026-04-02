import sys
from math import sqrt
from itertools import combinations


INF = 10 ** 8

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):

    # ================== 값 입력 받기
    
    N = int(input().rstrip())
    dots = []

    for _ in range(N):
        dots.append(list(map(int, input().rstrip().split())))
    
    # ================== 

    minLen = INF
    def dfs(curIdx, N, isPlus, plusNum):
        global dots, minLen
        
        if plusNum == N // 2:
            # 계산
            result = [0, 0]
            for i in range(N):
                if isPlus[i]:
                    result[0] += dots[i][0]
                    result[1] += dots[i][1]
                else:
                    result[0] -= dots[i][0]
                    result[1] -= dots[i][1]
            
            minLen = min(minLen, sqrt(result[0] ** 2 + result[1] ** 2))
            return
        
        if N - curIdx == (N//2) - plusNum:
            # 전부다 플러스로 연산
            result = [0, 0]
            for i in range(curIdx):
                if isPlus[i]:
                    result[0] += dots[i][0]
                    result[1] += dots[i][1]
                else:
                    result[0] -= dots[i][0]
                    result[1] -= dots[i][1]
            for i in range(curIdx, N):
                result[0] += dots[i][0]
                result[1] += dots[i][1]
            
            minLen = min(minLen, sqrt(result[0] ** 2 + result[1] ** 2))
            return

        
        dfs(curIdx+1, N, isPlus, plusNum)
        
        isPlus[curIdx] = True
        dfs(curIdx+1, N, isPlus, plusNum + 1)
        isPlus[curIdx] = False

    dfs(0, N, [False]*N, 0)

    print(F"{minLen}\n")