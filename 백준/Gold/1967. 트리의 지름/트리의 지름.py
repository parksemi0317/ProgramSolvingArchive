import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

edges = {}

for i in range(N):
    edges[i+1] = []

for i in range(N-1):
    parent, child , weight = map(int, input().rstrip().split())

    edges[parent].append((child, weight))


dp = [(0, 0) for _ in range(N)] # (자식 노드까지의 최대 거리 , 자신을 허리로 하는 거리)
def dfs(cur):

    global edges
    childs = edges[cur]

    max_depth = sec_depth = 0
    for c, w in childs:
        temp = dfs(c) + w
        if temp > max_depth:
            max_depth, sec_depth = temp, max_depth
        elif temp > sec_depth:
            sec_depth = temp
    dp[cur-1]= (max_depth, max_depth+ sec_depth)
    return max_depth

dfs(1)

print(F"{max([max(d) for d in dp ])}")
        

    