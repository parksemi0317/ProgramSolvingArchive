import sys

input = sys.stdin.readline

# =========== 값 입력 받기 ===========
G = int(input().rstrip())
P = int(input().rstrip())

planes = []
for _ in range(P):
    planes.append(int(input().rstrip()))

# =========== 함수 ===========

# 해당 값이 들어왔을 때 도킹할 수 있는 가장 큰 게이트 번호
# -1인 경우 더이상 게이트가 없는 상황
gates = [i for i in range(G+1)]

def findRoot(gate):
    if gate == 0:
        return -1
    
    root = gate
    while gates[root] != root:
        if gates[root] == -1:
            gates[gate] = -1
            return -1
        root = gates[root]
    gates[gate] = root # 평탄화
    return root
    

def dockToGate(gate): 
    global gates
    
    # 현재 게이트의 대체 게이트 찾기
    if gates[gate] == gate:
        gates[gate] = findRoot(gate-1)
    else:
        gates[gate] = findRoot(gates[gate])

# =========== 풀이 ===========

result = 0
for p in planes:

    dockGate = findRoot(p)
    if dockGate == -1:
        # 더이상 게이트가 없는 경우 종료
        break
        
    dockToGate(dockGate)
    # print(f"{p}를 {dockGate}gate에 도킹 완료 => {gates}")
    result += 1
print(result)
    