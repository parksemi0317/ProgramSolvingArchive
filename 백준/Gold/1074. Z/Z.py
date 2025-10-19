import sys

input = sys.stdin.readline
print = sys.stdout.write

N , r, c = map(int, input().rstrip().split())

# print(f"[Debug] N : {N} , r : {r} , c : {c}\n\n")

result = 0

def searchZ(N, baseX, baseY):
    global result, r, c

    if N == 0:
        print(f"{result}")
        return
    
    if c < baseX + 2 ** (N-1):
        if r < baseY + 2 ** (N-1):
            # 1사분면에 위치한 경우
            searchZ(N-1, baseX, baseY)
        else:
            # 3사분면에 위치한 경우
            result += (2 ** (N-1)) * (2 ** (N-1)) * 2
            searchZ(N-1, baseX, baseY +2 ** (N-1))
    elif r < baseY + 2 ** (N-1):
        # 2사분면에 위치한 경우
        result += (2 ** (N-1)) * (2 ** (N-1))
        searchZ(N-1, baseX +2 ** (N-1), baseY)
    else:
        # 4사분면에 위치한 경우
        result += (2 ** (N-1)) * (2 ** (N-1)) * 3
        searchZ(N-1, baseX +2 ** (N-1), baseY +2 ** (N-1))

searchZ(N, 0, 0)