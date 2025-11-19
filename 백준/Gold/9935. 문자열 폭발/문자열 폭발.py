import sys

input = sys.stdin.readline
print = sys.stdout.write


str = input().rstrip()
bomb = input().rstrip()
bomb_len = len(bomb)

my_stack = []
stack_len = 0
for c in str:
    my_stack.append(c)
    stack_len += 1
    if stack_len >= bomb_len and ''.join(my_stack[stack_len - bomb_len:]) == bomb:
        for _ in range(bomb_len):
            my_stack.pop()
        stack_len -= bomb_len

if my_stack:
    print(f"{''.join(my_stack)}")
else:
    print("FRULA")