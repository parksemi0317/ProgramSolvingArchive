import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

names = ["" for _ in range(N)]
idx = {}

for i in range(N):
    name = input().rstrip()
    names[i] = name
    idx[name] = i

for _ in range(M):
    temp = input().rstrip()
    # print(f"[DEBUG] temp : {temp} => ")

    if temp[0] > "0" and temp[0] <= "9":
        print(f"{names[int(temp)-1]}\n")
    else:
        print(f"{idx[temp] + 1}\n")