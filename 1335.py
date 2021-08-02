while True:
    n = int(input())
    if n == 0:
        break
    word_list = []
    for i in range(n):
        word = input()
        word_list.append(word)
    ans = ""
    first_word = word_list[0]
    word_list.remove(first_word)
    total = 0
    for i in range(len(first_word)):
        ans += first_word[i]
        for wd in word_list:
            if ans in wd:
                if len(ans) == len(wd):
                    word_list.remove(ans)
                elif len(ans) == len(first_word) and wd.startswith(first_word):
                    total += (len(wd) - len(ans))
                    word_list.remove(wd)
                continue
            else:
                total += len(wd)
                word_list.remove(wd)
    print(total)

#15% wrong answer