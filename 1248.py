n = int(input())
while n != 0:
    n -= 1
    diet = input()
    breakfast = input()
    lunch = input()
    x = []
    for i in range(len(diet)):
        if diet[i] in breakfast:
            continue
        elif diet[i] in lunch:
            continue
        else:
            x.append(diet[i])
    if len(x)+len(lunch)+len(breakfast) == len(diet):
        x.sort()
        ans = ""
        for i in range(len(x)):
            ans += x[i]
        print(ans)
    else:
        print("CHEATER")