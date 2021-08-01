while True:
    try:
        n = input()
        number_list = '1234567890'
        flag = 0
        ans = ""
        for i in range(len(n)):
            if n[i] in number_list:
                ans += n[i]
            else:
                if n[i] == "l":
                    ans += "1"
                elif n[i] == 'o' or n[i] == 'O':
                    ans += "0"
                elif n[i] != ',' and n[i] != ' ':
                    flag = 1
                    break
        try:
            ans = int(ans)
            if ans > 2147483647:
                flag = 1
        except ValueError:
            ans = "error"

        if flag:
            ans = "error"
        print(ans)
    except EOFError:
        break