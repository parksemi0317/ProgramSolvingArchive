def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        for startIdx in range(s, s+l):
            for endIdx in range(startIdx, s+l):
                num = int(str[startIdx : endIdx+1])
                if num > k:
                    answer.append(num)
    return answer