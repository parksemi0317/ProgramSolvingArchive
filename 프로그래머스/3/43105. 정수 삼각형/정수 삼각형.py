def solution(triangle):

    for line in range(1, len(triangle)):
        triangle[line][0] += triangle[line-1][0]
        
        
        for i in range(1, line):
            triangle[line][i] += max(triangle[line-1][i-1], triangle[line-1][i])
        triangle[line][-1] += triangle[line-1][-1]
    return max(triangle[-1])