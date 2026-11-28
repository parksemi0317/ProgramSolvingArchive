N, M,  L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]

xList = [x for x, _ in stars]
yList = [y for _, y in stars]

result = 0
for x in xList:
    for y in yList:

        cnt = 0
        for star in stars:
            if x <= star[0] <= x+L and y <= star[1] <= y+L:
                cnt += 1

        result = max(result, cnt)
print(K-result)