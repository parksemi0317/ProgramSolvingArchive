def solution(people, limit):
    people.sort()
    s = 0
    l = len(people)-1
    result = 0
    while s<l:
        if people[s] + people[l] <= limit:
            s += 1
        l -= 1
        result +=1
    if s==l:
        result += 1
    return result