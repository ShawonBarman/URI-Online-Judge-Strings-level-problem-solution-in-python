while True:
    try:
        inp = input()
        l, r = inp.split("+")
        r, j = r.split("=")
        if j.isalpha():
            print(int(l) + int(r))
        elif l.isalpha():
            print(int(j) - int(r))
        elif r.isalpha():
            print(int(j) - int(l))
    except EOFError:
        break