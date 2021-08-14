while True:
    try:
        words = (input().lower()).split("-")
        if len(words) == 5:
            test = "cobol"
            ans = ""
            for i in range(5):
                if words[i].startswith(test[i]) or words[i].endswith(test[i]):
                    ans += test[i]
            if ans == "cobol":
                print("GRACE HOPPER")
            else:
                print("BUG")
    except EOFError:
        break