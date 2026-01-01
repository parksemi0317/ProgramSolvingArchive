import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

def dfs(cur):
    global arr, dp, path
    dp[cur-1] = -1
    path.append(cur)

    next = arr[cur-1]
    if dp[next-1] != 0:
        if next in path:
            # print("[DEBUG] cycle 발견\n")
            # 사이클 발견
            startIdx = path.index(next)
    
            for std in path[startIdx :]:
                dp[std-1] = 1
    else:
        dfs(next)


for _ in range(T):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))

    # print(f"\n========================\n[DEBUG] arr : {arr}\n")

    dp = [0 for _ in range(N)] # 0 : 방문 x / 1 : cycle / -1 : 방문 O (사이클 X)
            
    for i in range(N):
        if dp[i] == 0:
            path = []
            dfs(i+1)
            
    # print(f"[DEBUG] dp : {dp}\n")
    print(f"{dp.count(-1)}\n")