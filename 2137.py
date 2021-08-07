while True:
    try:
        n = int(input())
        arr = []
        while n != 0:
            n -= 1
            code = input()
            arr.append(code)
        arr.sort()
        for i in arr:
            print(i)
    except EOFError:
        break