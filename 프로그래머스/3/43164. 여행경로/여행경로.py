def dfs(usedCnt, current, cityArr, visit, tickets, tNum):
    if usedCnt == tNum:
        return cityArr + [current]
    
    for i in range(tNum):
        if not visit[i] and tickets[i][0] == current:
            
            visit[i] = True
            tmp = dfs(usedCnt+1, tickets[i][1], cityArr + [tickets[i][0]], visit, tickets, tNum)
            if tmp != False:
                return tmp
            visit[i] = False
    return False
            
def solution(tickets):
    tickets.sort() # tickets 정렬
    
    tNum = len(tickets)
    visit = [False] * tNum
    
    return dfs(0, "ICN", [], [False] * tNum,tickets, tNum)