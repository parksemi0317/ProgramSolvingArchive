import sys
from bisect import insort_left, bisect_left, bisect_right


input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int, input().rstrip().split())

# ================ 누적합 구하기
nums = [0] * N # 입력된 기본 숫자 (인덱스)
prefixSum = [0] * (N + 1) # 누적합 (번째)

for i in range(N):
    num = int(input().rstrip())
    nums[i] = num
    prefixSum[i+1] = prefixSum[i] + num

# print(F"[DEBUG] nums : {nums}\n")
# print(F"[DEBUG] prefixSum : {prefixSum}\n")
# ================ 

changed = {}
sortedCKey = []

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split())
    # print(F"\n ===== {a}, {b}, {c}\n")
    if a == 1:
        # 수 바꾸기
        if not (b in changed): # 시간초과 뜨면 sortedCKey에서 이분탐색 돌려서 찾기!
            insort_left(sortedCKey, b)
        changed[b] = c

        # print(F"[DEBUG] changed : {changed}\n")
        # print(F"[DEBUG] sortedCKey : {sortedCKey}\n")
        
    else:
        # 출력하기
        prevResult = prefixSum[c] - prefixSum[b-1]
        
        bIdx = bisect_left(sortedCKey, b)
        cIdx = bisect_right(sortedCKey, c)

        # print(F"[DEBUG] bIdx : {bIdx}\n")
        # print(F"[DEBUG] cIdx : {cIdx}\n")
        for idx in range(bIdx, cIdx):
            i = sortedCKey[idx]
            prevResult -= nums[i-1]
            prevResult += changed[i]

        print(F"{prevResult}\n")