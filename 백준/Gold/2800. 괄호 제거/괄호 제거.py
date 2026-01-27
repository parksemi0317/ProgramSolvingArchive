import sys
from collections import deque

print = sys.stdout.write

inputStr = input()
# print(F"[Debug] inputStr : {inputStr}\n")

parentheses = [-1 for _ in range(len(inputStr))] # 괄호 id값 가지고 있음
setCount = 0
q = deque([])

for i, c in enumerate(inputStr):
    if c == "(":
        q.append(i)
    elif c == ")":
        prevI = q.pop()
        parentheses[prevI] = parentheses[i] = setCount
        setCount += 1
        
        
# print(f"[DEBUG] parentheses : {parentheses}\n")

result = set([])
for bitMask in range((0b1 << setCount) -1):
    # print(f"[DEBUG] bitMask : {bitMask}\n")

    tempStr = ""

    for i, pIdx in enumerate(parentheses):
        if pIdx == -1:
            tempStr += inputStr[i]

        elif (bitMask >> pIdx) & 0b1 > 0:
            tempStr += inputStr[i]
    # print(f"[DEBUG] {tempStr}\n")
    result.add(tempStr)

for s in sorted(list(result)):
    print(f"{s}\n")

    
    
