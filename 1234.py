while True:
    try:
        word = input()
        x = len(word)
        ans = ""
        i = 0
        while i < len(word):
            if word[i] == " ":
                ans += " "
                i += 1
            else:
                ans += word[i].upper()
                if i+1 < x:
                    if word[i+1] == " ":
                        i += 1
                        while word[i] == " ":
                            ans += word[i]
                            i += 1
                        if word[i] != "":
                            ans += word[i].lower()
                            i += 1
                    else:
                        ans += word[i + 1].lower()
                        i += 2
                else:
                    i += 1
        print(ans)
    except EOFError:
        break