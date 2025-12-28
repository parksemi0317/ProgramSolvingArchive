import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

MAX = 1000000001 * 3

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

minus = []
minus_cnt = 0
plus = []
plus_cnt = 0
for i in arr:
    if i < 0:
        minus_cnt += 1
        minus.append(i)
    else:
        plus_cnt += 1
        plus.append(i)

plus.sort() # 오름차순 정렬
minus.sort() # 오름차순 정렬

if minus_cnt == 0:
    # 양수만 있는 경우
    print(f"{plus[0]} {plus[1]} {plus[2]}")
elif plus_cnt == 0:
    # 음수만 있는 경우
    print(f"{minus[-3]} {minus[-2]} {minus[-1]}")
else:
    # 양수와 음수가 섞여 있는 경우
    result = MAX
    result_sets = []

    def checkResult(a, b, c):
        global result, result_sets

        temp =abs(a+b+c)
        if temp < result:
            result = temp
            result_sets = [a, b, c]
        
    
    def solution():
        global minus_cnt, plus_cnt, minus, plus, result, result_sets

        
        # 양수만 3개
        if plus_cnt >= 3:
            checkResult(plus[0], plus[1], plus[2])
        # 음수만 3개
        if minus_cnt >= 3:
            checkResult(minus[-3], minus[-2], minus[-1])
        if result == 0:
            return

        # 양수 1개, 음수 2개
        if minus_cnt > 1:
            minus_combs = list(combinations(minus, 2))
            # print(f"===== [DEBUG] plus : {plus}\n")
        
            for a, b in minus_combs:
                # print(f"[DEBUG] a, b :{a}, {b} (합  : {a+b})")
                cIdx = bisect_left(plus, -a-b)
                # print(f" => cIdx : {cIdx}\n")

                if cIdx < plus_cnt:
                    checkResult(a, b, plus[cIdx])
                if cIdx - 1 >= 0:
                    checkResult(a, b, plus[cIdx-1])
                if cIdx + 1 < plus_cnt:
                    checkResult(a, b, plus[cIdx+1])

                if result == 0:
                    return
            
    
        # 양수 2개, 음수 1개
        # print(f"===== [DEBUG] minus : {minus}\n")
        if plus_cnt > 1:
            plus_combs = list(combinations(plus, 2))
    
            for a, b in plus_combs:
                # print(f"[DEBUG] a, b :{a}, {b} (합  : {a+b})")
                cIdx = bisect_left(minus, -a-b)
                # print(f" => cIdx : {cIdx}\n")

                if cIdx < minus_cnt:
                    checkResult(a, b, minus[cIdx])
                if cIdx - 1 >= 0:
                    checkResult(a, b, minus[cIdx-1])
                if cIdx + 1 < minus_cnt:
                    checkResult(a, b, minus[cIdx+1])

                if result == 0:
                    return
        
    solution()                  
    for i in sorted(result_sets):
        print(f"{i} ")
        
    