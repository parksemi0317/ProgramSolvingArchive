import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

def print_arr(arr_str, is_reverse, start, end):
    result = arr_str[start : end+1]
    if is_reverse:
        result.reverse()
        
    print("[")
    print(",".join(result))
    print("]\n")
    

def check(p, n, arr_str):
    is_reverse = False
    start = 0
    end = n-1
    
    for opt in p:
        # print(f"[Debug] ")
        # print_arr(arr_str, is_reverse, start, end)
        if opt == "R":
            is_reverse = not is_reverse
        if opt == "D":
            if start > end:
                print("error\n")
                return
            if is_reverse:
                # 뒤집힌 경우 -> end 한칸 앞으로
                end -= 1
            else:
                # 뒤집히지 않은 경우  -> start 한칸 뒤로
                start += 1
    print_arr(arr_str, is_reverse, start, end)

    
for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())

    arr_str = []
    if n ==0:
        # print(f"\n[Debug] arr_str : {arr_str}, p : {p}\n")
        _ = input().rstrip()
    else :
        arr_str = list(input().rstrip()[1: -1].split(","))
        # print(f"\n[Debug] arr_str : {arr_str}, p : {p}\n")
    check(p, n, arr_str)
    