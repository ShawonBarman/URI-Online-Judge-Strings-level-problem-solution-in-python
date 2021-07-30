while True:
    try:
        w = input()
        p = int(input())
        sum = 0
        x = p
        for i in range(len(w)):
            if w[i] == "R":
                if x == p:
                    sum += 1
                elif x == 0:
                    x = p
                    sum += 1
                x -= 1
            elif w[i] == "W":
                sum += 1
                x = p
        print(sum)

    except EOFError:
        break