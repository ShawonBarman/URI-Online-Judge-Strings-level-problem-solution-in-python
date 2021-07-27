def calculate(n):
    if n == 0:
        return 6
    elif n == 1:
        return 2
    elif n == 2:
        return 5
    elif n == 3:
        return 5
    elif n == 4:
        return 4
    elif n == 5:
        return 5
    elif n == 6:
        return 6
    elif n == 7:
        return 3
    elif n == 8:
        return 7
    elif n == 9:
        return 6

num = int(input())
while num != 0:
    num -= 1
    sum = 0
    inp = input()
    for i in range(len(inp)):
        sum += calculate(int(inp[i]))
    print(sum,"leds")