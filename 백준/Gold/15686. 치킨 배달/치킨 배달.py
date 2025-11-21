import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

homes = []
home_cnt = 0
chicks = []
chick_cnt = 0

for i in range(N):
    line = list(input().rstrip().split())

    for j in range(N):
        if line[j] == "2":
            chicks.append((i, j))
            chick_cnt += 1
        elif line[j] == "1":
            homes.append((i, j))
            home_cnt += 1

distances = [[0 for _ in range(chick_cnt)] for _ in range(home_cnt)]

for i in range(chick_cnt):
    for j in range(home_cnt):
        dx = homes[j][0] - chicks[i][0] if homes[j][0] > chicks[i][0] else chicks[i][0] - homes[j][0]
        dy = homes[j][1] - chicks[i][1] if homes[j][1] > chicks[i][1] else chicks[i][1] - homes[j][1]
        
        distances[j][i] = dx + dy

chick_idx_sets = list(combinations(range(chick_cnt), M))


result = 2 * N * chick_cnt * home_cnt + 1
for comb in chick_idx_sets:
    new_val = 0
    for i in range(home_cnt):
        new_val += min([distances[i][j] for j in comb])
    result = min(new_val, result)

print(f"{result}")
            
    

