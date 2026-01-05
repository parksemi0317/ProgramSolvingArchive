import sys
from bisect import bisect_left

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

result = [arr[0]]

for num in arr[1:]:
    if result[-1] < num:
        result.append(num)
    else:
        idx = bisect_left(result, num)
        result[idx] = num


print(F"{len(result)}")