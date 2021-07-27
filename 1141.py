while True:
    n = int(input())
    if n == 0:
        break
    input_list = []
    while n != 0:
        n -= 1
        inp = input().lower()
        input_list.append(inp)
    maxi = -999999
    for i in range(len(input_list)-1):
        if input_list[i] in input_list[i + 1]:
            if len(input_list[i]) > maxi:
                maxi = len(input_list[i])
    if maxi == -999999:
        maxi = len(input_list)
    print(maxi)

#30% wrong solution