while True:
    try:
        n, y = input().split()
        n = int(n)
        arr = []
        for i in range(n):
            name = input().split()
            password = ""
            for nm in name:
                password += nm[0]
            password += y
            if password not in arr:
                arr.append(password)
        print(n - len(arr))
    except EOFError:
        break