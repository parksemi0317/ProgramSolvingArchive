import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())


arr = []

for _ in range(N):
    s, e = map(int, input().rstrip().split())
    arr.append((e, s))

arr.sort()

time = 0
cnt = 0

# print(f"[Debug] arr : {arr}\n")

for (e, s) in arr:
    if time <= s:
        # print(f"[Debug] {s}부터 {e}까지 회의 진행\n")
        time = e
        cnt +=1
        

print(f"{cnt}")