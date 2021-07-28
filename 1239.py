while True:
    try:
        text = input()
        x = True
        y = True
        ans = ""
        for i in range(len(text)):
            if text[i] == "_":
                if x == True:
                    ans += "<i>"
                    x = False
                else:
                    ans += "</i>"
                    x = True
            elif text[i] == "*":
                if y == True:
                    ans += "<b>"
                    y = False
                else:
                    ans += "</b>"
                    y = True
            else:
                ans += text[i]
        print(ans)
    except EOFError:
        break