n = int(input())
while n != 0:
    n -= 1
    k = int(input())
    arr = []
    for i in range(k):
        langu = input()
        arr.append(langu)
    main = arr[0]
    for i in arr:
        if i == main:
            continue
        else:
            main = "ingles"
            break
    print(main)