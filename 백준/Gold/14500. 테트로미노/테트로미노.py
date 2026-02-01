import sys
import heapq
INF = 10 ** 9

input = sys.stdin.readline
print = sys.stdout.write

# ================ 값 입력 받기 ================

N, M = map(int, input().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# ================ 테트로미노 구하기 ================

base1 = [(0, 0), (0, 1), (0, 2)]
add1 = [(-1, 0), (-1, 1), (-1, 2), (1, 0), (1, 1), (1, 2), (0, 3)]

base2 = [(0, 0), (1,0), (2, 0)]
add2 = [(0, -1), (1, -1), (2, -1), (0, 1), (1, 1), (2, 1), (3, 0)]

base3 = [(0, 0), (1, 0), (1, 1)]
add3 = [(0, -1), (0, 1), (2, 1)]

base4 = [(0, 0), (1, 0), (0, 1)]
add4 = [(-1, 1), (1 , -1)]

tetrominos = [(base1, add1),
             (base2, add2),
             (base3, add3),
             (base4, add4)]
 
# ================ 최대 테트로미노 구하기 ================
result = 0
# resultBoxes = []
for i in range(N):
    for j in range(M):

        for base, add in tetrominos:

            baseSum=0
            for box in base:
                nextI, nextJ = i + box[0], j +  box[1]
                if 0 <= nextI < N and 0 <= nextJ < M:
                    baseSum += board[nextI][nextJ]
                else:
                    baseSum = -INF
                    break
            
            if baseSum > 0:
                for box in add:
                    nextI, nextJ = i + box[0], j +  box[1]
                    if 0 <= nextI < N and 0 <= nextJ < M:
                        result = max(result, baseSum + board[nextI][nextJ])
                        
                        # if result == baseSum + board[nextI][nextJ]:
                        #     resultBoxes = base + [box]

print(f"{result}\n")
# print(f"{resultBoxes}")
                    