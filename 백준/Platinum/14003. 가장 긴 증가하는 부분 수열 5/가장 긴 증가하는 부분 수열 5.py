import sys
from bisect import bisect_left
INF = 1000000001

input = sys.stdin.readline
print = sys.stdout.write

# ============= 값 입력 받기 =============

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

# ============= dp 구하기 =============

tail = [] # tail[len] : 길이가 len+1인 LIS의 마지막 값 최소
# tail에 해당하는 arr배열 내 index 정보
tailIdx = [] # tailIdxList[len] : idx => arr[idx] == tail[len]

prev = [-1 for i in range(n)] # 각 arr 배열의 값들에 대하여 증가 수열을 구성하는 이전 arr내 index 정보

for idx, num in enumerate(arr):

    bisPos = bisect_left(tail, num)

    if bisPos >= len(tail):
        tail.append(num)
        tailIdx.append(idx)
    else:
        tail[bisPos] = num
        tailIdx[bisPos] = idx

    if bisPos > 0:
        prev[idx] = tailIdx[bisPos-1]


# ============= 정답 출력하기 =============

listLen = len(tail)
print(F"{listLen}\n")

result = []
idx = tailIdx[-1]

while idx != -1:
    result.append(arr[idx])
    idx = prev[idx]

for num in reversed(result):
    print(F"{num} ")
