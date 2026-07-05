def canTest(duration, n, times):
    cnt = 0
    for t in times:
        cnt += duration // t
    return cnt >= n

def solution(n, times):
    s = 0
    e = 1000000000 * 1000000000
    
    while s < e:
        mid = (s+e)//2
        if canTest(mid, n, times):
            e = mid
        else:
            s = mid + 1
    return s