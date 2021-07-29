while True:
    try:
        tag = input()
        new_tag = input()
        document = input()
        ans = ""
        x = False
        i = -1
        while i < len(document)-1:
            i += 1
            if document[i] == "<":
                x = True
                print("<",end="")
                continue
            elif document[i] == ">":
                x = False
                print(">",end="")
                continue

            if x and document[i].lower() == tag[0].lower() and i+len(tag) < len(document):
                ignore = True
                for j in range(1, len(tag)):
                    if tag[j].lower() != document[i+j].lower():
                        ignore=False
                        break
                if ignore:
                    print(new_tag,end="")
                    i += len(tag) - 1
                    continue
                else:
                    print(document[i],end="")
                    continue
            print(document[i],end="")
        print()
    except EOFError:
        break
