def solution(routes):
    
    answer = 1
    
    routes.sort(key=lambda x :x[1])
    cam = routes[0][1]
    for s, e in routes:
        if cam < s:
            answer += 1
            cam = e
    return answer