while True:
    n = int(input())
    if n == 0:
        break
    while n != 0:
        n -= 1
        one = 0
        zero = 0
        k = input()
        for i in range(len(k)):
            if i % 2 == 0:
                zero += int(k[i])
            else:
                one += int(k[i])
        result = 0
        while zero != 0:
            result += (zero % 10)
            zero = int(zero/10)
        while one != 0:
            result += (one % 10)
            one = int(one/10)
        print(result)