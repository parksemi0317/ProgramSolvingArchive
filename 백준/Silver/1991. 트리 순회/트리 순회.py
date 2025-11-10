import sys

input =  sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

edges = {}

for _ in range(N):
    p, l, r = input().rstrip().split()

    edges[p] = [l, r]

# ========= 전위 순회
def pre(e):
    print(f"{e}")

    for child in edges[e]:
        if child != ".":
            pre(child)
    
pre("A")
print("\n")

# ========= 중위 순회
def mid(e):
    l ,r = edges[e]
    
    if l != ".":
        mid(l)
    print(f"{e}")
    
    if r != ".":
        mid(r)

mid("A")
print("\n")

# ========= 후위 순회

def back(e):

    for child in edges[e]:
        if child != ".":
            back(child)
    print(f"{e}")
    
back("A")
print("\n")