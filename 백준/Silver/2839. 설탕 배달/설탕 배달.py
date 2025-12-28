def sol(n):
    for fiveBasket in range(n//5, -1, -1):
        left = n - 5 * fiveBasket

        if left % 3 == 0:
            print(int(fiveBasket + left/3))
            return
    print(-1)

n = int(input())

sol(n)