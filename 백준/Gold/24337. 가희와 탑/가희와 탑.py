import heapq
    
def sol():
    N, a, b = map(int, input().split())

    if a + b - 1 > N:
        print(-1)
        return

    stack = [i for i in range(1, a+1)]

    if stack[-1] < b:
        stack[-1] = b

    stack += [i for i in range(b-1, 0, -1)]

    left = N - (a+b-1)
    stack = [stack[0]] + [1 for _ in range(left)]+ stack[1:]
    

    for i in stack:
        print(i, end=" ")

sol()