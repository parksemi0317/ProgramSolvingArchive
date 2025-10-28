import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

is_connected = {}

for _ in range(N-1):
    x, y = map(int, input().rstrip().split())

    if x in is_connected:
        is_connected[x].append(y)
    else:
        is_connected[x] = [y]

    if y in is_connected:
        is_connected[y].append(x)
    else:
        is_connected[y] = [x]
# print(f"[Debug] is_connected : {is_connected}")


parent = [0 for _ in range(N)]

def searchChild(k):
    global is_connected, parent
    
    for i in is_connected[k]:
        if parent[i-1] == 0:
            parent[i-1] = k
            searchChild(i)

searchChild(1)

for i in range(1, N):
    print(f"{parent[i]}\n")
