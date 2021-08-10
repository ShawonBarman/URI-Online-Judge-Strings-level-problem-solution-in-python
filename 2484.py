while True:
    try:
        text = list(input())
        temp = len(text)
        x = 1
        while len(text) != 1:
            temp -= 1
            for i in range(len(text)-1):
                print(text[i],end=" ")
            print(text[len(text)-1])
            print(" "*x,end="")
            text.pop()
            x += 1
        print(text[0])
        print()
    except EOFError:
        break