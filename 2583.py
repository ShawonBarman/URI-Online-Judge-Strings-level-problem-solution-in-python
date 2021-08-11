c = int(input())
while c != 0:
    c -= 1
    n = int(input())
    arr = []
    while n != 0:
        n -= 1
        x, y = input().split()
        if y == "chirrin":
            if x not in arr:
                arr.append(x)
        elif y == "chirrion":
            if x in arr:
                arr.remove(x)
    arr.sort()
    print("TOTAL")
    for i in arr:
        print(i)