def solution(s):
    cnt = 0
    for c in s:
        if c == "p" or c == "P":
            cnt += 1
        elif c == "y" or c =="Y":
            cnt -= 1
    return cnt == 0