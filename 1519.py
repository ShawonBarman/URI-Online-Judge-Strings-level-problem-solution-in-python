while True:
    text = input().lower()
    if text == ".":
        break
    text = text.split()
    dic = {}
    arr = []
    count = 0
    for i in range(len(text)):
        if (len(text[i]) == 1 and text[i][0] == 'e') or (len(text[i]) == 2 and text[i][0] == 'e') or (len(text[i]) == 3 and text[i][0] == 'e'):
            arr.append(text[i])
        else:
            x = text[i][0] + "."
            dic.update({x:text[i]})
            arr.append(x)
            count += 1
    print(arr[0],end="")
    for i in range(1, len(arr)):
        print(" {}".format(arr[i]),end="")
    print()
    print(count)
    for i in sorted(dic.keys()):
        print(i, "=", dic[i])

# wrong solution. i just try