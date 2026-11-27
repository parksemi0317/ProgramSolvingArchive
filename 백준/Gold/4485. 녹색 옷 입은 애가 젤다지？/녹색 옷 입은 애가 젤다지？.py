from collections import deque
INF = 10 ** 9
MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))

pNum = 1
while True:
    n = int(input())

    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[INF for _ in range(n)]for _ in range(n)]
    dp[0][0] = board[0][0]
    
    q = deque([(0, 0, board[0][0])])
    while q:
        x, y, num = q.popleft()
        for mx, my in MOVES:
            newX, newY = x+mx, y+my
            
            if newX < 0 or newX >= n or newY < 0 or newY >= n:
                continue

            newNum = num + board[newX][newY]
            if newNum < dp[newX][newY]:
                dp[newX][newY] = newNum
                q.append((newX, newY, newNum))

    print(f"Problem {pNum}: {dp[n-1][n-1]}")
    # for line in dp:
    #     print(line)
    # print()
    pNum += 1