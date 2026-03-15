import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

# ============ 값 입력 받기 ============
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
opts = []

for _ in range(M):
    opts.append(list(map(int, input().rstrip().split())))

# opts.sort(key=lambda x: x[2]) # 비용기준으로 정렬

# print(F"[DEBUG] opts : \n")
# for i, opt in enumerate(opts):
#     print(F"[{i}] : {opt}\n")
# print("\n")

# ============  ============
sortedA = tuple(sorted(A)) # 정답

def solution():
    hq = [(0, tuple(A))] # (비용, 현재 배열, 디버깅용 opt idx 배열)
    isInserted = {} # 얼마의 비용으로 해당 배열이 만들어졌는지 정보  
    
    isInserted[tuple(A)] = 0
    
    while hq:
        # print(f"\n[DEBUG] hq : {hq}\n")
        curCost, curA = heapq.heappop(hq)
        # print(f"[DEBUG] curA  : {curA}, debugArr : {debugArr}\n")
    
        if curA == sortedA: # 비내림차순이 완성된 경우
            # print(f"{debugArr}\n")
            return curCost

        if isInserted[curA] < curCost: # 중복 제거
            continue

        for l, r, c in opts:
            newA = list(curA)
            newA[l-1], newA[r-1] = newA[r-1], newA[l-1]

            newA = tuple(newA)
            
            if not newA in isInserted:
                heapq.heappush(hq, (curCost+c, newA))
                isInserted[newA] = curCost + c
            elif isInserted[newA] > curCost + c:
                heapq.heappush(hq, (curCost+c, newA))
                isInserted[newA] = curCost + c
    return -1

print(F"{solution()}")
                