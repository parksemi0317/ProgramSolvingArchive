T = int(input())

def getFact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


for _ in range(T):
    n = int(input())
    # print(f"\n======== [Debug] n : {n} ==========")
    maxThree = n // 3

    result = 0
            
    for threeCnt in range(maxThree, -1, -1):
        maxTwo = (n - threeCnt * 3) // 2
        for twoCnt in range(maxTwo, -1, -1):
            oneCnt = n - threeCnt * 3 - twoCnt * 2

            result += getFact(threeCnt + twoCnt+ oneCnt) // (getFact(threeCnt) * getFact(twoCnt) * getFact(oneCnt))

    print(result)