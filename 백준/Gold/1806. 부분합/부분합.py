import sys
INF = 100001

input = sys.stdin.readline
print = sys.stdout.write


N, S = map(int, input().rstrip().split())


arr = list(map(int, input().rstrip().split()))


start = 0
end = 0
sum = arr[0]
result = INF
while 1:
    if sum >= S: 
        result = min(result, end - start + 1)
        # 한칸 더 줄여보기
        if start < end:
            sum -= arr[start]
            start+=1
            continue
    # 총 합이 적거나 더 줄일 수 없는 경우
    if end < N-1:
        end += 1
        sum += arr[end]
    else:
        break
print(f"{0 if result >= INF else result}")