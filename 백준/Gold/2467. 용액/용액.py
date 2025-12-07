from itertools import combinations
import sys

print = sys.stdout.write
INF = 1000000000 * 100001

N = int(input())


waters = list(map(int, input().split()))

minusCnt = 0
while minusCnt < N and waters[minusCnt] < 0:
    minusCnt+=1
# print(f"[DEBUG] minusCnt : {minusCnt}\n\n")

if minusCnt == N:
    # 음수 밖에 없는 경우
    print(f"{waters[-2]} {waters[-1]}")
elif minusCnt == 0:
    # 양수 밖에 없는 경우
    print(f"{waters[0]} {waters[1]}")
else:
    # 양수와 음수가 섞여 있는 경우
    resultDiff = INF
    result = []
    minusIdx = minusCnt - 1
    plusIdx = minusCnt
    while minusIdx >= 0 and plusIdx < N:
        sum = waters[minusIdx] + waters[plusIdx]
        diff = sum if sum > 0 else -sum 

        if resultDiff > diff:
            resultDiff = diff
            result = (waters[minusIdx],waters[plusIdx])

        if sum > 0:
            minusIdx -= 1
        elif sum < 0:
            plusIdx += 1
        else:
            # print(f"{result[0]} {result[1]}")
            break

    # 음수 두개와 비교
    if minusCnt >= 2 and -waters[minusCnt-2] - waters[minusCnt-1] < resultDiff:
        resultDiff = -waters[minusCnt-2] - waters[minusCnt-1]
        result = (waters[minusCnt-2],waters[minusCnt-1])

    # 양수 두개와 비교
    if N - minusCnt >= 2 and waters[minusCnt] + waters[minusCnt+1] < resultDiff:
        resultDiff  =  waters[minusCnt] + waters[minusCnt+1]
        result = ( waters[minusCnt] , waters[minusCnt+1])
        
    print(f"{result[0]} {result[1]}")