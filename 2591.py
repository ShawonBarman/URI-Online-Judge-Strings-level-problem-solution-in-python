n = int(input())
while n > 0:
    n -= 1
    c = input().split("me")
    # print(c)
    a = (c[0].count("a") * c[1].count("a")) * "a"
    print("k{}".format(a))