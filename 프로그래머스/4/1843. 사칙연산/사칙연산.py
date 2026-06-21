from collections import deque
INF = 10 ** 6

def solution(arr):
    
    numCnt = (len(arr) + 1) // 2
    nums = [int(arr[i*2]) for i in range(numCnt)] # 숫자 배열
    opts = [arr[i*2 +1] for i in range(numCnt -1)] # 연산자 배열
    # print("nums", nums)
    # print("opts", opts)
    
    
    minDP = [[nums[i] if i == j else INF for i in range(numCnt)] for j in range(numCnt)]
    maxDP = [[nums[i] if i == j else -INF for i in range(numCnt)] for j in range(numCnt)]
    
    for size in range(2, numCnt+1): # 합치려는 숫자 수
        # print(f"====== [DEBUG] size : {size} ======")
        
        for start in range(numCnt - size+1): # 시작 숫자 idx
            # print(f"[DEBUG] start:{start}, {nums[start: start+size]}")
            
            for optNum in range(size-1): # 몇번째 opt로 합칠 것인가
                maxNum1 = maxDP[start][start+optNum]
                maxNum2 = maxDP[start+optNum+1][start+size-1]
                minNum1 = minDP[start][start+optNum]
                minNum2 = minDP[start+optNum+1][start+size-1]
                opt = opts[optNum + start]
                
                if opt == '-':
                    maxDP[start][start+size-1] = max(maxDP[start][start+size-1], maxNum1-minNum2)
                    minDP[start][start+size-1] = min(minDP[start][start+size-1], minNum1-maxNum2)
                else:
                    maxDP[start][start+size-1] = max(maxDP[start][start+size-1], maxNum1+maxNum2)
                    minDP[start][start+size-1] = min(minDP[start][start+size-1], minNum1+minNum2)

    return maxDP[0][numCnt-1]
    
    