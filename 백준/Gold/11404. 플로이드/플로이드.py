import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip()) # 도시 개수
m = int(input().rstrip()) # 버스 개수

INF = 100001 * m

distance = [[0 if i==j else INF for j in range(n)] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    distance[a-1][b-1] = min(c, distance[a-1][b-1])
    
for mid in range(n):
    for s in range(n):
        for e in range(n):
            distance[s][e] = min(distance[s][e], distance[s][mid] + distance[mid][e])
        
for line in distance:
    for dist in line:
        print(f"{0 if dist >= INF else dist} ")
    print("\n")