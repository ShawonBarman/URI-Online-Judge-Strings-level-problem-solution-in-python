n = int(input())
while n != 0:
    n -= 1
    inp = input().split("x")
    x = int(inp[0])
    y = int(inp[1])
    if x == y:
        for i in range(5,11):
            print("{} x {} = {}".format(x, i, x*i))
    else:
        for i in range(5,11):
            print("{} x {} = {} && {} x {} = {}".format(x, i, x*i, y, i, y*i))