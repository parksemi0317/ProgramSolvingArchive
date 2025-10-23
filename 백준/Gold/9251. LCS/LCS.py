import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

str1 = input().rstrip()
str1_len = len(str1)
str2 = input().rstrip()
str2_len = len(str2)


arr = [[0 for _ in range(str1_len)] for _ in range(str2_len)]

for idx in range(str2_len):
    if str1[0] == str2[idx]:
        for i in range(idx, str2_len):
            arr[i][0] = 1
        break

for idx in range(str1_len):
    if str2[0] == str1[idx]:
        for i in range(idx, str1_len):
            arr[0][i] = 1
        break

for x in range(1, str2_len):
    for y in range(1, str1_len):
        
        if str2[x] == str1[y]:
            arr[x][y] = arr[x-1][y-1]+1
        else:
            arr[x][y] = max(arr[x-1][y], arr[x][y-1])

print(f"{arr[-1][-1]}")
        

    