import sys

input = sys.stdin.readline
print = sys.stdout.write

NONE = -1

C, N = map(int, input().rstrip().split())

ads = []

for _ in range(N):
    ads.append(list(map(int, input().rstrip().split())))

dp = [[(0 if i == 0 else NONE) for i in range(C+1)] for _ in range(N)]

def printDP():
    global dp

    for dist in range(0, C+1):
        print(f"{dist}".rjust(4))
    print("\n" + "-"*(C+1)*4 + "-\n")
    
    for line in dp:
        for d in line:
            print(f"{d}".rjust(4))
        print("\n")
    print("\n")

# printDP()


for targetC in range(1, C):
    for i in range(N):

        cost, effect = ads[i]

        if targetC < effect:
            continue

        prev = targetC - effect
        tmp = []
        tmpCnt = 0
        for j in range(N):
            if dp[j][prev] != NONE:
                tmp.append(dp[j][prev])
                tmpCnt +=1

        if tmpCnt == 0:
            continue
        dp[i][targetC] = min(tmp) + cost

# printDP()

for i in range(N):
    cost, effect = ads[i]

    tmp = []
    start = max(C-effect, 0)
    for prev in range(start, C):
        for j in range(N):
            if dp[j][prev] != NONE:
                tmp.append(dp[j][prev])

    
    totalMin = min(tmp)
    dp[i][C] = totalMin + cost

# printDP()

print(f"{min(filter(lambda x : x != NONE ,[dp[i][C] for i in range(N)]))}")
        
    