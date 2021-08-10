while True:
    try:
        n = int(input())
        ans = 0
        while n != 0:
            n -= 1
            species = input()
            breed = input()
            name = input().split()
            input()
            if (len(name) > 1) and (species == 'cachorro'):
                for i in name:
                    if i[0] == breed[0]:
                        ans += 1
                        break
        print(ans)

    except EOFError:
        break