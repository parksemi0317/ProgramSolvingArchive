def solution(number, k):
    stack = []
    
    for num in number:
        # 스택에 값이 있고, k가 남았고, 현재 숫자보다 스택 마지막 숫자가 작으면 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        
        stack.append(num)
    
    # 만약 k가 남았다면 뒤쪽을 잘라냄
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)