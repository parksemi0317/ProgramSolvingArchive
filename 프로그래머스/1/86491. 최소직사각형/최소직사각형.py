def solution(sizes):
    for s in sizes:
        s.sort(reverse=True)
        
    # print(sizes)
    
    width = max([ s[0] for s in sizes])
    height = max([s[1] for s in sizes])
    
    return width * height