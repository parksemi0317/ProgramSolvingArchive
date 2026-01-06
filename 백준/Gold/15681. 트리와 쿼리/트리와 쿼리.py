import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
print = sys.stdout.write

N, R, Q = map(int, input().rstrip().split())

connecteds = {}

for i in range(1, N+1):
    connecteds[i] = []

for _ in range(N-1):
    U, V = map(int, input().rstrip().split())
    connecteds[U].append(V)
    connecteds[V].append(U)

dp = [-1 for _ in range(N)]

def countSubTree(root, parent):
    global dp, connecteds
    
    if dp[root-1] != -1:
        return dp[root-1]
    result = 1
    for child in connecteds[root]:
        if child != parent:
            result += countSubTree(child, root)
    dp[root-1] = result
    return result


countSubTree(R, -1)
for _ in range(Q):
    U = int(input().rstrip())

    print(f"{dp[U-1]}\n")

    