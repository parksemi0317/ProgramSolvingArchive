import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

dp_cost = [[0 for _ in range(N)] for _ in range(3)]


r, g, b = map(int, input().rstrip().split())
dp_cost[0][0] = r
dp_cost[1][0] = g
dp_cost[2][0] = b

for i in range(1, N):
    rgb_arr = list(map(int, input().rstrip().split()))

    for j in range(3):
        dp_cost[j][i] = min(dp_cost[(j+1)%3][i-1] , dp_cost[(j+2)%3][i-1]) + rgb_arr[j]

print(F"{min(dp_cost[0][N-1], dp_cost[1][N-1], dp_cost[2][N-1])}")
    