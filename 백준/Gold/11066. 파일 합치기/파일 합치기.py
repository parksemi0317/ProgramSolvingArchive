import sys
INF = 10 ** 9

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for t in range(T):
    # print(f"\n\n=========== {t} ===========\n")
    K = int(input().rstrip())
    
    files = list(map(int, input().rstrip().split()))
    prefixSum = [0 for _ in range(K+1)]

    for i in range(K):
        prefixSum[i+1] = prefixSum[i] + files[i]

    # print(F"[DEBUG] files : {files}\n")
    # print(F"[DEBUG] prefixSum : {prefixSum}\n")

    dp = [[INF for _ in range(K)] for _ in range(K)]

    # def printDp():
    #     for line in dp:
    #         for c in line:
    #             print(F"{c if c < INF else "INF"}".rjust(5))
    #         print("\n")
    #     print("\n")
    
    # print(f"===== [DEBUG] len : 1 & 2 =====\n")
    for i in range(K):
        dp[i][i] = 0
        
    for i in range(K-1):
        dp[i][i+1] = files[i] + files[i+1]
    
    # printDp()
    
    for len in range(3, K+1):
        # print(f"===== [DEBUG] len : {len} =====\n")
        for start in range(K):
            end = start + len - 1
            if end >= K:
                continue;
            # print(f"[DEBUG] start : {start}, end : {end}\n")
            for mid in range(start, end):
                # print(f"[DEBUG] {start} {mid} {end} : {dp[start][mid]}+{dp[mid+1][end]}+{prefixSum[end+1] - prefixSum[start]}={dp[start][mid] + dp[mid+1][end] + prefixSum[end+1] - prefixSum[start]}\n")
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + prefixSum[end+1] - prefixSum[start])
        # printDp()
    
    # printDp()
    print(F"{dp[0][K-1]}\n")
        