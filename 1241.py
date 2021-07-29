n = int(input())
while n != 0:
    n -= 1
    a, b = input().split()
    x = len(a)
    y = len(b)
    if x < y:
        print('nao encaixa')
    else:
        if a[(x - y):] == b:
            print('encaixa')
        else:
            print('nao encaixa')