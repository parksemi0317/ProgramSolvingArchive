import heapq
    
def sol():
    N, a, b = map(int, input().split())

    # 불가능한 경우
    if a + b - 1 > N:
        print(-1)
        return

    # 왼쪽에서 봤을때 최소 합(1 2 ... a)으로 먼저 넣기
    stack = [i for i in range(1, a+1)]

    # 오른쪽에서 봤을 때 기준 마지막 빌딩 높이가 부족하면 마지막 빌딩만 바꾸기
    if stack[-1] < b:
        stack[-1] = b

    # 오른쪽에서 봤을 때 최소 합 (b b-1 ... 1)로 넣기
    stack += [i for i in range(b-1, 0, -1)]

    # 남은 개수만큼 두번째 자리에 1로 다 넣기
    left = N - (a+b-1)
    stack = [stack[0]] + [1 for _ in range(left)]+ stack[1:]
    
    # 결과 출력
    for i in stack:
        print(i, end=" ")

sol()