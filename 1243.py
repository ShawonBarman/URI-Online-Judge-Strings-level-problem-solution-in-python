while True:
    try:
        word = input().split()
        i = 0
        while i < len(word):
            for ch in word[i]:
                if ch.isdigit():
                    del word[i]
                    i -= 1
                    break
            if len(word) > 0 and word[i].count('.') > 1:
                del word[i]
                i -= 1
            i += 1
        count = 0
        for i in word:
            if (i.count(".") == 0) or (i.index(".") == len(i)-1):
                count += len(i)
            if "." in i:
                count -= 1
        if len(word) == 0:
            avg = 0
        else:
            avg = count // len(word)
        if avg <= 3:
            print(250)
        elif avg == 4 or avg == 5:
            print(500)
        else:
            print(1000)
    except EOFError:
        break