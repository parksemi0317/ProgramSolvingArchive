import sys

n = int(input())

count = 0
cols = [False] * n
up_left = [False] * (n*2 - 1) # x - y 값 동일 (-n+1 ~ n-1)
up_right = [False] * (n*2 - 1) # x + y 값 동일 (0 ~ 2n-2)

def check(i_idx):
    global n, rows, cols, up_left, up_right, count
        
    for j in range(n):
        if not cols[j]and not up_right[i_idx + j] and not up_left[i_idx - j + n - 1]:

            if i_idx == n-1:
                count += 1
                return
            
            cols[j] = True
            up_right[i_idx + j] = True
            up_left[i_idx - j + n - 1] = True
            
            check(i_idx+1)
            
            cols[j] = False
            up_right[i_idx + j] = False
            up_left[i_idx - j + n - 1] = False

check(0)
print(count)