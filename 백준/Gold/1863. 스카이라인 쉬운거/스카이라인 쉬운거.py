
n = int(input())
s = [0] # 스택
result = 0
for _ in range(n):
    x, y = map(int, input().split())

    if s[-1] < y: # 이전 값보다 큰 경우 스택에 쌓기
        s.append(y)
    elif y == 0: # 바닥이 보인 경우 이전 묶음에서의 값 정리하고 스택 초기화
        result += len(s) - 1 # 0이 기본으로 들어있기에 -1
        s = [0]
    else: # 이전 값보다 작은 경우 해당 높이보다 높은 건물들 정리하기
        while s[-1] > y:
            s.pop()
            result +=1 
        if s[-1] == y:
            s.pop()
        s.append(y)
        
result += len(s) - 1 # 아직 스택에 남은 건물들 정리하기

print(result)