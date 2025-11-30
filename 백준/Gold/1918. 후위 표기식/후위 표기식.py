import sys
from collections import deque
OPTS = (("*", "/"), ("+", "-"))

mids = deque(input())

def getBack(mids):
    global OPTS
    
    for opt in OPTS:
        # print(f"\n[DEBUG] opt : {opt}")
        s = deque([])
    
        num1 = ""
        mum2 = ""
        while mids:
            c = mids.popleft()
            if c in opt:
                num1 = s.pop()
                num2 = mids.popleft()
                s.append(num1 + num2 + c)
            else:
                s.append(c)
        mids = s
        # print(f"[DEBUG] s : {s}")
    return mids

def calParenth(mids):
    # print(f"\n[DEBUG] calParenth({mids})")
    s = deque([])
    while mids:
        c = mids.popleft()

        if c == "(":
            # 새로운 괄호 시작
            recur = calParenth(mids)
            # print(f"[DEBUG] 새로운 괄호 발견 : {recur}")
            s.append(recur)
            # print(f"[DEBUG] s :{s}, mids :{mids}")
        elif c == ")":
            # 현재 괄호 종료 -> 반환
            result = getBack(s)
            # print(f"[DEBUG] result : {result}\n")
            return result[0]
        else:
            s.append(c)
            # print(f"[DEBUG] s :{s}, mids :{mids}")
    return getBack(s)
result = getBack(calParenth(mids))
print(list(result)[0])
            
            