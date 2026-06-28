from collections import deque

def getRoot(nodes, indegrees, outdegrees):
    for n in nodes:
        if indegrees[n][0] == 0 and outdegrees[n][0] >= 2:
            return n

# 해당 그래프의 모양 구하기
# 1 : 도넛, 2 : 막대, 3 : 8자
def getShape(start_node, root_node, nodes, indegrees, outdegrees):
    q = deque([start_node])
    visit = {start_node : 1}
    while q:
        cur_node = q.popleft()
        
        if outdegrees[cur_node][0] == 0:
            return 2 # 막대 그래프
        if outdegrees[cur_node][0] == 2:
            return 3 # 8자 그래프
        
        for next_node in outdegrees[cur_node][1]:
            if next_node not in visit:
                q.append(next_node)
                visit[next_node] = 1
    return 1
    
    
    

def solution(edges):
    # indegree, outdegree, node 목록 가공
    indegrees = {}
    outdegrees = {}
    nodes = {}
    for f, t in edges:
        if f not in nodes:
            indegrees[f] = [0, []]
            outdegrees[f] = [0, []]
            nodes[f] = 1
        if t not in nodes:
            indegrees[t] = [0, []]
            outdegrees[t] = [0, []]
            nodes[t] = 1
        outdegrees[f][0] += 1
        outdegrees[f][1].append(t)
        indegrees[t][0] += 1
        indegrees[t][1].append(f)
        
    # root 구하기
    root_node = getRoot(nodes, indegrees, outdegrees)
    answer = [root_node, 0, 0, 0]
    # root와 연결되어 있는 각 그래프의 shape 구하기
    for start_node in outdegrees[root_node][1]:
        shape_idx = getShape(start_node, root_node, nodes, indegrees, outdegrees)
        answer[shape_idx] += 1
    return answer
        
        
        
    