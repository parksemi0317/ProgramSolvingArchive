import sys

input = sys.stdin.readline
print = sys.stdout.write

# =========== 값 입력 받기

N, L, R = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# =========== 데이터 가공

# 연합 찾기
def findDisjoints():
    global L, R, board
    
    roots = [i*N + j for i in range(N) for j in range(N)]
    
    def findRoot(n):
        if roots[n] == n:
            return n
        roots[n] = findRoot(roots[n])
        
        return roots[n]
    
    # 가로
    for i in range(N):
        for j in range(N-1):
            if L <= board[i][j] - board[i][j+1] <= R or L <= board[i][j+1] - board[i][j] <= R:
                a = i*N + j
                b = i*N + j+1
                aRoot = findRoot(a)
                bRoot = findRoot(b)
                if aRoot < bRoot:
                    roots[bRoot] = aRoot
                else:
                    roots[aRoot] = bRoot

    # 세로
    for j in range(N):
        for i in range(N-1):
            if L <= board[i][j] - board[i+1][j] <= R or L <= board[i+1][j] - board[i][j] <= R:
                a = i*N + j
                b = (i+1)*N + j
                aRoot = findRoot(a)
                bRoot = findRoot(b)
                if aRoot < bRoot:
                    roots[bRoot] = aRoot
                else:
                    roots[aRoot] = bRoot
    group = {}
    for i in range(N):
        for j in range(N):
            root = findRoot(i*N + j)

            if root in group:
                group[root][0] += 1
                group[root][1].append(i*N+j)
            else:
                group[root] = [1, [i*N+j]]
    result = []
    for root in group:
        if group[root][0] > 1:
            result.append(group[root][1])
    # print(F"[DEBUG] {result}\n")
    return result

# =========== 데이터 가공

groups = findDisjoints()

day = 0
while groups:
    day += 1

    for g in groups:
        sum = 0
        cnt = 0
        for i in g:
            sum += board[i//N][i%N]
            cnt += 1

        for i in g:
            board[i//N][i%N] = sum // cnt
    
    groups = findDisjoints()

print(F"{day}")