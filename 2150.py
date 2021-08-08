while True:
    try:
        vouwel = input()
        text = input()
        count = 0
        for i in vouwel:
            count += text.count(i)
        print(count)
    except EOFError:
        break