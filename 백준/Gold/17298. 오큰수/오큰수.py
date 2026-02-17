import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))
s = deque([0]) # 아직 오큰수를 찾지 못한 수들의 idx 목록 (내림차순으로 정렬되어 들어감)
result = [-1 for _ in range(N)] # 결과

idx = 1
while s and idx < N:

    while s and arr[idx] > arr[s[-1]]:
        result[s[-1]] = arr[idx]
        s.pop()
    s.append(idx)
    idx += 1

for c in result:
    print(f"{c} ")
    